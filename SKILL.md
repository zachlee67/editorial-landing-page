---
name: editorial-landing-page
description: >-
  Build a single self-contained HTML landing page in XEDEA's editorial house style for ANY
  industry (home services, real estate, education/tuition, professional services/agencies,
  F&B, e-commerce/DTC, SaaS, and more) — not just aesthetic clinics. Use this when the operator
  asks for "a landing page like the clinic one but for [other business]", "no AI slop landing
  page", "pain-point landing page", or wants XEDEA's specific style: editorial serif headings, a
  pain-point-led hero that still names the product/service, no small "eyebrow" labels above
  headings, no em/en dashes used as sentence connectors, a concern/pain-point card grid, a
  mechanism or process explainer, a benefits grid, a primary vs secondary offer comparison table
  when there are two related offers, an FAQ accordion, a sticky contact CTA (WhatsApp by
  default in Malaysia/Singapore), and a lead form placed at the very end of the page. For a
  Malaysia/Singapore aesthetic clinic or medical aesthetic treatment specifically, prefer
  `aesthetic-clinic-landing-page` instead, which has the clinic-specific interview questions and
  a fully worked clinic example already built in. For a landing page where the operator wants a
  different visual language entirely (not this editorial serif house style) or wants the broader
  research-driven section-pattern library, use the general `landing-page` skill instead.
---

# Editorial Landing Page

This is the industry-agnostic sibling of `aesthetic-clinic-landing-page`. Same structural DNA
and the same house style rules, generalized so any business can use it, not just clinics. It
exists because the underlying pattern (pain-point hero, alternating-background sections, no AI
tells, form-always-last) turned out to work for reasons that have nothing to do with medicine —
they're about how a real person reads a page before they act on it.

Read `references/industry-section-map.md` before building for any industry — it maps each
generic slot in the skeleton to what that slot actually means for that vertical, based on 2026
conversion research. If the operator's industry isn't listed there, do the same kind of quick
search ("[industry] landing page best practices") before guessing at the mapping, and consider
adding your findings back to that file for next time.

`assets/reference-template.html` is the same worked example used by `aesthetic-clinic-landing-page`
(all client-identifying details replaced with generic placeholders). It's a structural/CSS
reference, not a fill-in-the-blank template — read it to understand the patterns, then build a
new file with the industry's own section meanings and the operator's own brand.

## Step 1: Interview before building anything

Do not start writing HTML until you know:

1. **Industry** — this determines which row of `references/industry-section-map.md` applies,
   and therefore what several of the skeleton's generic sections should actually contain (or
   whether they should be dropped).
2. **Primary offer** — the product/service/treatment/course/listing, its mechanism or process
   (how it actually works or what the engagement looks like), and its 1-2 headline USPs (what
   makes it different from the next competitor's page).
3. **Secondary offer, if any** — some businesses want a second, related offer mentioned at lower
   weight (a companion service, an add-on package, a second product tier). If there is one, plan
   for a comparison table between the two, placed after both are individually explained and
   before the proof section (before/after, case studies, or gallery, depending on the industry).
4. **The pain-point angle.** A page that just states "we do X" reads like every competitor's
   brochure. Propose 3-4 distinct emotional angles a real customer might feel (fear of a bad
   outcome, frustration that nothing else has worked, being caught off guard by a moment that
   forced the decision, wanting a subtle/low-risk first step, time pressure/urgency) with an
   example headline for each, and let the operator pick or blend. The hero headline should still
   name the actual offer somewhere prominent (helps ad message-match/quality score), even when
   it's built around an emotional hook rather than a literal description.
5. **Pricing/promo policy** — starting price shown in the CTA itself (e.g. "Book Now, From
   RM999" or "Starting at $49/mo"), a promo/discount banner, or no price at all (drive everyone
   to enquire)?
6. **Contact channel and brand assets** — WhatsApp is the safe default for Malaysia/Singapore
   consumer and SMB businesses, but confirm: some verticals convert better on a calendar-booking
   link (higher-ticket professional services), a "start free trial"/demo request (SaaS), or a
   direct checkout (e-commerce). Also get the WhatsApp number or booking link, logo, existing
   site URL (scrape it for real brand colors/fonts/copy if one exists), and whether photos/videos
   are ready now or should be left as clearly-labeled placeholders. Default to placeholders
   rather than stock photos, except in verticals (F&B, home services, e-commerce) where the
   section-map flags real photos as a launch blocker rather than something you can placeholder
   around.
7. **Competitor references** — actively ask for these, don't just wait for the operator to
   volunteer them: "Do you have 3-5 competitor landing pages you like the feel of?" Real
   competitor URLs are one of the highest-signal inputs you can get; the clinic vertical this
   skill descends from came from an operator who supplied 4 competitor pages upfront, and that's
   what made the section order and tone land right on the first draft. If they have any, fetch
   all of them (not just one or two) and note each one's section order, hero pattern, and tone.
   Do not copy phrasing verbatim, and do not treat a reference page as gospel if the operator's
   own established style (from a prior round of feedback) disagrees with it, ask which should
   win. If they have none, proceed without, but still ask.

Ask these one at a time or in a short batch, whichever fits the conversation, but get real
answers before generating a full page. A page built on assumptions gets thrown out and redone.

## Step 2: The house style rules

These came from direct user feedback across many iterations on the original clinic vertical, and
they generalize cleanly. Bend them only when the operator explicitly asks for the exception:

- **No small "eyebrow" label above headings** (no `"— SOME LABEL"` sitting above an `<h1>`/`<h2>`).
  It was tried, the operator disliked it everywhere, and it was removed site-wide. Headings stand
  alone.
- **No em/en dash used to join two clauses** in a sentence (the "word — and" or "word—word"
  pattern reads as AI-generated). Rewrite as two sentences, or use a comma/colon instead. Number
  ranges (`2-3 months`, `RM999-1499`, `9am-6pm`) are fine, that's a different use of the dash and
  isn't the tell the operator reacts to.
- **Hero pattern**: pain-point-led headline that still names the actual offer, a short paragraph
  naming the frustration/fear/moment and resolving it, an optional checklist of recognizable
  signs (per the industry map), and **one** clear CTA (not two competing buttons). If a price is
  part of the offer, put it in the CTA button label itself rather than as a separate line.
- **Section flow** (adapt names per `references/industry-section-map.md`, keep the shape): Hero
  → trust strip (credibility badges relevant to the industry) → "is this you" pain-point cards →
  mechanism/process explainer → benefits grid → offer-details section → \[secondary offer, if
  any: its own intro, its own explainer, its own benefits, all as separate `<section>`s with
  alternating backgrounds, not one crammed block\] → comparison table (if two offers) → proof
  section (before/after, case studies, or a photo gallery, per the industry map) →
  credibility/why-us → testimonials (placeholder, never fabricated) → FAQ accordion → final CTA
  → lead form (always last, unless the industry map says otherwise for a low-friction signup
  flow) → footer.
- **Alternate section backgrounds** (light/white/brand-tinted) section by section, the way a
  real editorial page breathes, rather than several consecutive sections sharing one background
  with no visual break.
- **FAQ accordion**: animate with `grid-template-rows: 0fr → 1fr` on the answer wrapper, not
  `max-height`. Animating `max-height`/`height`/`padding` causes layout thrash;
  `grid-template-rows` is compositor-friendly and gives the same visual collapse/expand.
- **Sticky contact CTA**: fixed bottom-right, circular, brand color for the channel (WhatsApp
  green if that's the channel), with a subtle pulse animation, visible on every scroll position,
  linking with a pre-filled message relevant to the page's main offer. Swap the channel/style per
  Step 1's answer if it isn't WhatsApp.
- **Comparison table** (only when there's a secondary offer): a plain `<table>` with real
  distinguishing facts as rows (per the industry map: technology/method, depth/scope, best-for,
  sensation/experience, timeline, duration/longevity, price tier, whatever is actually true and
  different between the two), not marketing fluff repeated from the benefit cards above it.
- **Single self-contained HTML file**: inline `<style>` and `<script>`, Google Fonts via `<link>`
  (an editorial serif for headings + a clean sans for body; the reference uses Lora + Outfit, but
  match the operator's actual brand fonts if they have established ones), no build step, no
  framework, no tracking scripts unless the operator explicitly asks for a specific pixel/tag.
- **Never invent proof.** Before/after images, testimonials, credentials, case-study numbers, and
  review counts must come from the operator or their real site. If they're not available yet,
  leave a clearly labeled placeholder box, except where the industry map flags real assets as a
  hard launch blocker (food photography, literal project before/afters) rather than something a
  placeholder can stand in for.

## Step 3: Build

Write one HTML file per the structure above (adapted via the industry map), styled with the
operator's real brand colors (scrape their site if it exists, ask if not). Reuse the reference
template's proven CSS patterns (`.card-grid`/the concern-card pattern, `.benefit-grid`,
`.steps`/`.step-num`, the mini-benefits list, the comparison table, the FAQ accordion, the sticky
contact float) rather than reinventing them, but rename classes and rewrite every color/font/copy
value for the new brand and industry. Don't ship one industry's file with find-and-replaced text.

## Step 4: Verify before handing it back

Serve the file locally (a plain `python3 -m http.server` in its directory, or the Browser pane's
preview tools) and actually check, not just eyeball the code:
- The FAQ accordion opens/closes and is mutually exclusive.
- The form submit shows a thank-you state (if the form is present at all for this industry).
- The page stacks correctly at mobile width (375px), grids collapse to one column, nothing
  overflows horizontally.
- If a comparison table exists, it scrolls horizontally on narrow screens rather than breaking
  the layout.

## Step 5: Hand it off

Ask whether the operator wants it published as a shareable Claude Artifact link (fast, good for
internal review, not meant to carry real ad traffic) or just the raw `.html` file to hand to
whoever hosts it on the operator's actual domain (needed before it can take paid clicks, since it
will need real hosting plus any tracking tags the operator's media buyer adds separately).

## Relationship to the other two landing-page skills

- `aesthetic-clinic-landing-page`: use for Malaysia/Singapore aesthetic clinics and medical
  aesthetic treatments specifically. It has clinic-specific interview questions baked in and a
  fully worked example already built. This skill (`editorial-landing-page`) is everything else.
- `landing-page`: a separate, independent skill with its own research-driven section-pattern
  library and a different default visual style (eyebrow labels included). Use it when the
  operator wants that broader pattern-matching approach rather than this specific editorial house
  style, or when they haven't expressed a preference and you're not sure which fits, ask.
