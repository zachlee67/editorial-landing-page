# editorial-landing-page

[![Validate skill](https://github.com/zachlee67/editorial-landing-page/actions/workflows/validate.yml/badge.svg)](https://github.com/zachlee67/editorial-landing-page/actions/workflows/validate.yml)

A Claude Code / Claude.ai skill for building single-file HTML landing pages in an editorial
house style, for most industries: home services, real estate, education/tuition, professional
services/agencies, F&B, e-commerce/DTC, SaaS, and more.

Editorial serif headings, a pain-point-led hero that still names the offer, no small "eyebrow"
labels above headings, no em/en dashes used as sentence connectors, a pain-point card grid, a
mechanism/process explainer, a benefits grid, a primary vs secondary offer comparison table when
there are two related offers, an FAQ accordion, a sticky contact CTA, and a lead form at the very
end of the page. `references/industry-section-map.md` maps the generic skeleton onto what each
section actually means for a given industry. See `SKILL.md` for the full rules and interview
process.

## Install (for colleagues)

Claude Code and Claude.ai load skills from `~/.claude/skills/`. To use this skill:

1. Clone this repo somewhere on your machine:
   ```
   git clone https://github.com/zachlee67/editorial-landing-page.git
   ```
2. Copy (or symlink) the folder into your own skills directory:
   ```
   cp -r editorial-landing-page ~/.claude/skills/
   ```
   (On Windows / WSL, the equivalent Claude Code skills path applies, ask if you're not sure
   where that is on your machine.)
3. Restart Claude Code (or start a new session) so it picks up the new skill.
4. Ask Claude for what you want, see "How to prompt it" below for what to include.

## How to prompt it

Claude will interview you for anything you leave out (see Step 1 in `SKILL.md`), so a short
prompt still works. But naming your industry and offer clearly up front gets you a much closer
first draft, since it decides which row of `references/industry-section-map.md` to apply and
what several sections should actually contain (or whether to drop them).

**Copy-paste template.** Works across industries, replace every `[bracket]`, delete any line that
doesn't apply to you, and paste the whole thing:

> These are landing pages I like from competitors or similar businesses, please follow their
> UX/layout:
> - [competitor/reference landing page URL 1]
> - [competitor/reference landing page URL 2]
> - [competitor/reference landing page URL 3]
> (3-5 is ideal if you have them. If you don't have any yet, just say so, Claude will still ask
> what style/tone you want instead of guessing.)
>
> Now build me a landing page like the ones above, for my [industry] business, [Business Name].
> If I don't have photos or videos yet, just leave them as blank, clearly labeled placeholders
> for now.
>
> Here's my business's own website, use it for the real brand colors/fonts/logo: [your website
> URL]
>
> Primary offer: [service/product name]
> - Key benefits: [paste your offer's key benefits here]
> - USP: [paste what makes you different from competitors here]
>
> Secondary offer (optional, lower priority): [secondary offer name, or delete this whole section
> if there isn't one]
> - Key benefits: [paste key benefits here]
> - USP: [paste USP here]
>
> I want a high-converting landing page for [Google Ads/Meta Ads] in [country/market]. Mainly
> focus on [primary offer], with [secondary offer] mentioned at lower weight.
>
> No pricing shown. (Or: show "From [currency][X]" in the CTA button if you do want a starting
> price.)
>
> Contact channel is [WhatsApp / a calendar-booking link / a "start free trial" button / direct
> checkout], number or link is [number/url].
>
> Mainly optimize for [form submissions / whatever your main conversion goal is], but also add a
> floating [WhatsApp/contact] button if that fits. The form itself should sit at the very end of
> the page, not near the top.
>
> I don't want this to look AI-generated or like generic "AI slop."
>
> Ask me questions before you generate anything you're not sure about.

**What actually moves the output:**

- **Give 3-5 reference landing pages** if you have any you like the feel of. This is the
  highest-signal input you can give, far more useful than Claude guessing at what "good" looks
  like for your industry from general best-practice knowledge alone.
- **Name your industry explicitly** ("home services", "real estate", "tuition centre", "law
  firm", "SaaS", etc.). This is what tells Claude which section-mapping to use, home services
  gets literal before/after photos and WhatsApp, SaaS gets a product screenshot in the hero and
  "start free trial" instead of WhatsApp, F&B drops the mechanism-explainer section entirely for
  a food photo gallery. Naming the industry vaguely ("a business") loses all of that.
- **Say if there's a secondary offer.** That's what triggers the comparison-table section; without
  it, the page stays single-offer.
- **Say what pain point to lead with**, or ask Claude to propose 3-4 (fear of a bad outcome,
  "nothing else has worked," a moment that forced the decision, time pressure, etc.).
- **Confirm your contact channel.** WhatsApp is the default assumption for Malaysia/Singapore, but
  say if you actually want a calendar-booking link (professional services), "start a free trial"
  (SaaS), or a direct checkout (e-commerce) instead.
- **Point at your real website** if you have one, so brand colors/fonts get scraped for real
  instead of reusing the bundled example's demo palette.
- **Say what proof you don't have yet** (photos, case studies, reviews). The skill leaves these as
  labeled placeholders rather than inventing them, but only if you say what's missing.

**A minimal prompt also works, it just costs more back-and-forth:**

> Landing page for my [industry] business, [Business Name]. Ask me whatever you need.

Claude should reach for this skill automatically for a landing page request in this house style.
If it doesn't, invoke it directly with `/editorial-landing-page` or ask it to use the skill by
name.

## Updating

If you improve the skill (a new industry mapping, a better copy pattern, a fix), edit the files,
then:

```
git add -A
git commit -m "describe what changed"
git push
```

Everyone else picks up the change next time they `git pull` in their local clone and re-copy the
folder into `~/.claude/skills/` (or just work directly from a symlinked clone so `git pull` is
enough).

## Versioning: how to get an old version back

This repo is never force-pushed or rewritten once it's out (the one exception being a genuine
leaked-secret emergency, and even then, only with explicit sign-off first). Every meaningful
change gets a normal commit on top, plus a version tag, so nothing is ever lost:

```
git tag -a v1.1.0 -m "describe what changed in this version"
git push origin v1.1.0
```

We also cut a [GitHub Release](https://github.com/zachlee67/editorial-landing-page/releases)
from each tag so past versions show up in their own panel on GitHub, not just as commits.

**To get back an old version** six months from now (or any time):

```
git clone https://github.com/zachlee67/editorial-landing-page.git
cd editorial-landing-page
git checkout v1.0.0        # or whichever version you want
```

Or just browse the [Releases page](https://github.com/zachlee67/editorial-landing-page/releases)
on GitHub and download that version's source directly, no `git` needed.

Bump the version (`v1.0.0` → `v1.1.0` for a small change, `v2.0.0` for a rules-breaking change to
the house style or section map) whenever you tag. `main` always reflects the latest version;
every tagged version stays reachable forever alongside it.

## What it produces

A full worked example, built for a home-services business, to show the skill in action:

![Preview of the bundled example landing page](examples/preview.png)

Open `examples/aircon-servicing-demo.html` in a browser to see the full page (FAQ accordion,
sticky WhatsApp button, and form all work) rather than just the screenshot above. It's a
fictional demo business, not a real client.

## Contents

- `SKILL.md` — the skill's instructions: interview questions, house style rules, build/verify/
  handoff process, and how this skill relates to other landing-page skills.
- `references/industry-section-map.md` — how the generic section skeleton maps onto specific
  industries (home services, real estate, education, professional services, F&B, SaaS,
  e-commerce), sourced from 2026 conversion research. Add to this file as new industries come up.
- `examples/aircon-servicing-demo.html` + `examples/preview.png` — a full worked example (a
  fictional home-services business). Read it to understand the structural/CSS patterns, don't
  reuse its actual copy or colors for a real client, it's a worked example, not a fill-in-the-
  blank template.
- `scripts/validate_skill.py` — checks `SKILL.md` has valid frontmatter, every file referenced in
  `SKILL.md`/`README.md` actually exists, and that no real-looking phone/WhatsApp number or
  forbidden client name has crept into the repo. Run it yourself with
  `python3 scripts/validate_skill.py`; it also runs automatically on every push via
  `.github/workflows/validate.yml`.
- `LICENSE` — internal/proprietary, see the file for terms.
