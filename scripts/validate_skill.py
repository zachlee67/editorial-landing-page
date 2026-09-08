#!/usr/bin/env python3
"""Validate that this repo is a well-formed, safe-to-share Claude skill.

Checks:
1. SKILL.md exists and has valid YAML-ish frontmatter with `name` and `description`.
2. The frontmatter `name` matches the repo's own directory name.
3. Every relative file path referenced in SKILL.md/README.md (assets/..., references/...,
   examples/...) actually exists.
4. No real-looking Malaysia/Singapore phone or WhatsApp number is present anywhere in the
   repo, other than the known-safe placeholder numbers. This is the specific safeguard this
   skill family needs: reference/example templates should never carry a real client's
   contact info.
5. No forbidden client name appears anywhere in the repo, checked against a NORMALIZED
   version of each file: HTML tags stripped and URL-encoding decoded first. This exists
   because a real leak once hid as `<a class="logo">HN <span>Clinic</span></a>` (split
   across a tag) and `Hi%20HN%20Clinic%2C%20I...` (URL-encoded inside a wa.me link) - both
   invisible to a plain literal-string search. Never trust a plain grep for this class of
   check again; normalize first.

Exit code 0 = pass, 1 = fail. No third-party dependencies (stdlib only) so it runs in CI
with a bare `python3` and nothing else installed.
"""
import html
import re
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Numbers that are known placeholders, not real client data. Add to this list if you
# introduce a new placeholder pattern.
ALLOWED_PHONE_NUMBERS = {
    "60123456789",
    "012-345 6789",
    "+60123456789",
}

# Real client names/brands that must never appear anywhere in this repo, in any form
# (plain text, split across HTML tags, or URL-encoded). Add to this list whenever a real
# client's name is used as a worked example and then scrubbed, so it can't silently
# regress via a future edit or a copy/paste from an old draft.
FORBIDDEN_NAMES = [
    "hn clinic",
]

# Matches Malaysia/Singapore-style mobile numbers: 01X-XXXXXXX, +601XXXXXXXX, 601XXXXXXXX
PHONE_PATTERN = re.compile(r"(?:\+?60|0)1[0-9][-\s]?\d{3}[-\s]?\d{4,5}")

TEXT_EXTENSIONS = {".md", ".html", ".json", ".yml", ".yaml"}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    global had_failure
    had_failure = True


had_failure = False


def check_skill_md() -> dict:
    skill_md = REPO_ROOT / "SKILL.md"
    if not skill_md.exists():
        fail("SKILL.md not found at repo root")
        return {}

    text = skill_md.read_text()
    if not text.startswith("---"):
        fail("SKILL.md does not start with a '---' frontmatter block")
        return {}

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter block is not closed with a second '---'")
        return {}

    frontmatter_raw = parts[1]
    frontmatter = {}
    current_key = None
    for line in frontmatter_raw.splitlines():
        if not line.strip():
            continue
        if line.startswith(" ") or line.startswith("\t"):
            # continuation line (folded/multi-line YAML scalar), append to current key
            if current_key:
                frontmatter[current_key] = frontmatter.get(current_key, "") + " " + line.strip()
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            current_key = key.strip()
            frontmatter[current_key] = value.strip()

    if "name" not in frontmatter or not frontmatter["name"]:
        fail("SKILL.md frontmatter is missing a 'name' field")
    if "description" not in frontmatter or not frontmatter["description"]:
        fail("SKILL.md frontmatter is missing a 'description' field")

    return frontmatter


def check_name_matches_directory(frontmatter: dict) -> None:
    name = frontmatter.get("name", "").strip()
    expected = REPO_ROOT.name
    if name and name != expected:
        fail(f"SKILL.md name '{name}' does not match repo directory name '{expected}'")


def check_referenced_files_exist() -> None:
    ref_pattern = re.compile(r"`((?:assets|references|examples)/[A-Za-z0-9_.\-/]+)`")
    for doc in ("SKILL.md", "README.md"):
        doc_path = REPO_ROOT / doc
        if not doc_path.exists():
            if doc == "README.md":
                fail("README.md not found at repo root")
            continue
        text = doc_path.read_text()
        for match in ref_pattern.findall(text):
            if not (REPO_ROOT / match).exists():
                fail(f"{doc} references '{match}' but that file does not exist")


def check_no_real_phone_numbers() -> None:
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        for match in PHONE_PATTERN.findall(text):
            digits = re.sub(r"[^\d+]", "", match)
            if digits not in {re.sub(r"[^\d+]", "", n) for n in ALLOWED_PHONE_NUMBERS}:
                fail(
                    f"{path.relative_to(REPO_ROOT)} contains a phone-number-shaped string "
                    f"'{match}' that isn't the known placeholder. Confirm this isn't a real "
                    f"client number before committing."
                )


def check_no_forbidden_names() -> None:
    tag_pattern = re.compile(r"<[^>]+>")
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        if ".git" in path.parts:
            continue
        try:
            raw = path.read_text(errors="ignore")
        except Exception:
            continue
        # Normalize: decode URL-encoding, strip HTML tags (so text split across markup
        # like "HN <span>Clinic</span>" still reads as "HN Clinic"), collapse whitespace.
        decoded = urllib.parse.unquote(raw)
        decoded = html.unescape(decoded)
        no_tags = tag_pattern.sub(" ", decoded)
        normalized = re.sub(r"\s+", " ", no_tags).lower()
        for forbidden in FORBIDDEN_NAMES:
            if forbidden in normalized:
                fail(
                    f"{path.relative_to(REPO_ROOT)} contains the forbidden name '{forbidden}' "
                    f"once tags are stripped and URL-encoding is decoded. This must never "
                    f"reappear in this repo, check for it hiding across a tag boundary or in "
                    f"an encoded URL before committing."
                )


def main() -> int:
    frontmatter = check_skill_md()
    if frontmatter:
        check_name_matches_directory(frontmatter)
    check_referenced_files_exist()
    check_no_real_phone_numbers()
    check_no_forbidden_names()

    if had_failure:
        print("\nValidation FAILED.")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
