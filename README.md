# Talon Nail Bar — Site Build

A custom-coded site (no template, no site builder) for Talon Nail Bar,
509 S 4th St, Philadelphia, PA 19147.

## Files
- `index.html` — page structure and content
- `styles.css` — all styling
- `script.js` — mobile menu toggle (small, no dependencies)
- `assets/logo.png` — the real logo, used in the header, footer, and favicon
- `assets/hero-photo.jpg` — the hero's faded background image (see note
  below), resized/compressed from the original upload for page-load speed
- `assets/talon-logo-mark.svg` — a genuine vector trace of the real logo's
  linework and wordmark. Not currently used on the page, but kept here
  since it's a clean, scalable asset worth having around — e.g. for print
  materials or a future full-bleed treatment.
- `assets/hero-art.svg` — the earlier painted-nail botanical line art.
  Not currently used in the hero (swapped for the photo below), but kept
  here in case it's useful elsewhere, e.g. a smaller accent in the About
  or Book section.
- `generate_hero_art.py` — regenerates `assets/hero-art.svg` if you want
  to revisit that direction. Two separate random streams control it: `rng`
  (branch geometry) and `paint_rng` (nail color/accent choices).

## About the hero image
The hero background is a real photo (Unsplash-licensed, free for this kind
of commercial use, no rights issue) — chosen deliberately as a heavily
faded, blended backdrop rather than a claim about "our work." That's an
important distinction: a Gallery section showing "the work" needs to be
real photos of Talon's actual clients, and stock there would be
misleading — but a moody, faded hero backdrop is understood as atmosphere,
not a specific claim, the same way countless small business sites use
licensed photography as mood-setting background art. Don't reuse this
same reasoning to justify stock photos in the Gallery section — that's a
different context with a different expectation.

Technical notes:
- Cropped/positioned via `object-position: center 45%` to keep the actual
  manicure detail in frame — worth re-checking this value if the photo is
  ever swapped for a different one, since the right crop depends entirely
  on where the subject sits in that specific image.
- Faded via a combination of reduced opacity, a `saturate`/`brightness`
  filter (keeps it moody rather than a bright inserted photo), and a
  gradient scrim that's fully solid behind the copy and eases toward the
  photo further right.
- One CSS gotcha worth remembering for future edits: this section uses
  explicit `top/right/bottom/left: 0` rather than the shorter `inset: 0`
  — the shorthand isn't supported everywhere, and using it here silently
  broke the full-bleed background layer.

## Before showing this to the owner
1. **Gallery** (`#gallery` in index.html) — currently color swatches standing
   in for real photos. Swap in actual nail-art photos once you have them —
   drop image files in `assets/` and replace the `<div class="gallery-tile">`
   elements with `<img>` tags.
2. **Testimonials** (`#testimonials`) — currently marked
   `[Client testimonial to be added]`. Replace with real quotes once you
   have any — never leave fabricated quotes in their place.
3. **Booking button** — appears three times, each tagged with class
   `js-book-link` in the HTML so you can find them fast. Point these at
   the real GoHighLevel calendar link once it exists.
4. **Footer hours** — currently says "By appointment — message or call to
   confirm times," since we don't have their confirmed weekly hours.
   Update once you know them.
5. **About section copy** — written assuming continuity with the Best of
   Philly 2025 win. If it turns out to be new ownership, rewrite this
   paragraph live with the owner, the same way we planned for the
   GHL-template version.

## Deploying (GitHub Pages)
This is already live at the repo's GitHub Pages URL. To push an update:
1. Replace the changed files in your local working copy of the repo.
2. `git add .`
3. `git commit -m "describe what changed"`
4. `git push`

GitHub Pages picks up the change automatically within about a minute —
no separate build or deploy step needed, since this is plain HTML/CSS/JS.

## Notes on the design
- Colors, type, and layout choices are written up in the CSS file comments
  and match the brand's existing black-and-white identity from their
  Instagram.
- Built mobile-responsive, with keyboard focus states and reduced-motion
  support out of the box.
- No external dependencies beyond Google Fonts (Fraunces + Work Sans),
  loaded directly in `index.html`.
