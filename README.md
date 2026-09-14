# Talon Nail Bar — Site Build

A custom-coded site (no template, no site builder) for Talon Nail Bar,
509 S 4th St, Philadelphia, PA 19147.

## Files
- `index.html` — page structure and content
- `styles.css` — all styling
- `script.js` — mobile menu toggle (small, no dependencies)
- `assets/logo.png` — the real logo, used in the header, footer, and favicon
- `assets/hero-photo-crop.png` — the hero's image: a real photo, cropped
  and resized from the original upload, with a soft elliptical fade baked
  directly into the PNG's alpha channel (see note below) so it blends into
  the background instead of showing a hard rectangular edge. Sits in the
  right column of the two-column hero.
- `assets/talon-logo-mark.svg` — a genuine vector trace of the real logo's
  linework and wordmark. Not currently used on the page, but kept here
  since it's a clean, scalable asset worth having around — e.g. for print
  materials or a future full-bleed treatment.
- `assets/hero-art.svg` — the earlier painted-nail botanical line art.
  Not currently used in the hero (swapped for the photo), but kept here
  in case it's useful elsewhere, e.g. a smaller accent in the About or
  Book section.
- `generate_hero_art.py` — regenerates `assets/hero-art.svg` if you want
  to revisit that direction. Two separate random streams control it: `rng`
  (branch geometry) and `paint_rng` (nail color/accent choices).

## About the hero image
The hero image is a real photo (Unsplash-licensed, free for this kind of
commercial use, no rights issue) — used deliberately as a blended visual
element, not a claim about "our work." That's an important distinction:
a Gallery section showing "the work" needs to be real photos of Talon's
actual clients, and stock there would be misleading — but a photo used
this way, softly blended into the design, reads as visual atmosphere, not
a specific claim, the same way countless small business sites use
licensed photography this way. Don't reuse this same reasoning to justify
stock photos in the Gallery section — that's a different context with a
different expectation.

Technical notes:
- The soft edge is baked directly into the image's alpha channel (an
  elliptical fade, fully opaque through the center, feathering to fully
  transparent at the edges) rather than done with a CSS mask or filter.
  This was a deliberate choice for reliability — it renders correctly
  everywhere images render, with no dependency on a specific browser
  feature. If you ever swap in a different photo, you'll need to
  regenerate this fade rather than just dropping in a plain crop.
- Kept clear and vividly colored on purpose — an earlier full-bleed
  version that faded the whole photo down lost impact; this version
  keeps the photo itself at full clarity and only softens the edges.

## Files (services photos)
- `assets/service-dip-powder.jpg`, `assets/service-gel-manicure.jpg`,
  `assets/service-nail-art.jpg` — close-up crops pulled from the same hero
  photo (509 S 4th St shoot), used as the small icons in the Services list.
  Same reasoning as the hero image: real, licensed photography, used as
  illustrative detail rather than a "this is our work" claim — that claim
  is still reserved for the Gallery section once real studio photos exist.

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
