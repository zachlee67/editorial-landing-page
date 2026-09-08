# editorial-landing-page

A Claude Code / Claude.ai skill for building single-file HTML landing pages in XEDEA's editorial
house style, for any industry: home services, real estate, education/tuition, professional
services/agencies, F&B, e-commerce/DTC, SaaS, and more.

It's the industry-agnostic sibling of `aesthetic-clinic-landing-page` (originally built for a
Malaysia aesthetic clinic client): editorial serif headings, a pain-point-led hero that still
names the offer, no small "eyebrow" labels above headings, no em/en dashes used as sentence
connectors, a pain-point card grid, a mechanism/process explainer, a benefits grid, a primary vs
secondary offer comparison table when there are two related offers, an FAQ accordion, a sticky
contact CTA, and a lead form at the very end of the page. `references/industry-section-map.md`
maps the generic skeleton onto what each section actually means for a given industry. See
`SKILL.md` for the full rules and interview process.

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
4. Just ask Claude for what you want, e.g. *"Build me a landing page for [business]'s new
   [service], no pricing shown, WhatsApp number is [number]"* — Claude should reach for this
   skill automatically for a non-clinic landing page request in this house style. If it doesn't,
   invoke it directly with `/editorial-landing-page` (or ask it to use the skill by name).

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

## Contents

- `SKILL.md` — the skill's instructions: interview questions, house style rules, build/verify/
  handoff process, and how this skill relates to `aesthetic-clinic-landing-page` and the general
  `landing-page` skill.
- `references/industry-section-map.md` — how the generic section skeleton maps onto specific
  industries (home services, real estate, education, professional services, F&B, SaaS,
  e-commerce), sourced from 2026 conversion research. Add to this file as new industries come up.
- `assets/reference-template.html` — a structural/CSS reference (the same worked example used by
  `aesthetic-clinic-landing-page`, with all client-identifying details replaced by generic
  placeholders). Do not reuse its actual copy or colors for a real client, it's a worked example,
  not a fill-in-the-blank template.
