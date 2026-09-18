# Talon Nail Bar — Site Build

A custom-coded site (no template, no site builder) for Talon Nail Bar,
509 S 4th St, Philadelphia, PA 19147.

## Files
- `index.html` — page structure and content
- `styles.css` — all styling
- `script.js` — mobile menu toggle (small, no dependencies)
- `assets/logo.png` — the real logo, used in the header, footer, and favicon
- `assets/hero-photo-clean.jpg` — the hero's image, currently in use: a
  real photo of actual Talon client work (smiley-face + solid gel set),
  full frame, no feathering, with a plain 1px bronze border via CSS. Sits
  in the right column of the two-column hero.
- `assets/hero-photo-real.png` — the previous version of the same idea,
  with a soft elliptical fade baked into the alpha channel. No longer
  referenced in `index.html`, but kept here for reference/rollback.
- `assets/hero-photo-crop.png` — the earlier stock (Unsplash-licensed)
  photo originally used in this spot. No longer used now that a real photo
  exists, but kept here in case it's ever useful as a placeholder again.
- `assets/talon-logo-mark.svg` — a genuine vector trace of the real logo's
  linework and wordmark. Not currently used on the page, but kept here
  since it's a clean, scalable asset worth having around — e.g. for print
  materials or a future full-bleed treatment.
- `assets/hero-art.svg` — the earlier painted-nail botanical line art.
  Not currently used in the hero, but kept here in case it's useful
  elsewhere, e.g. a smaller accent in the About or Book section.
- `generate_hero_art.py` — regenerates `assets/hero-art.svg` if you want
  to revisit that direction. Two separate random streams control it: `rng`
  (branch geometry) and `paint_rng` (nail color/accent choices).

## About the hero image
The hero uses a real photo of actual Talon client work, not stock — full
frame, no feathering, just a clean 1px bronze border (`.hero-art-img` in
`styles.css`). Earlier passes tried an elliptical alpha-fade to blend the
photo into the dark background; that's been dropped in favor of showing
the photo as-is, clearly and rectangularly — simpler, and it reads as more
credible than an art-directed fade would.

One framing note: the source photo is landscape (945×691) and both hands'
outer fingers reach almost to the frame edges, so it isn't cropped to a
tighter portrait shape — that would clip the pinky nails on one or both
hands. It's used at full frame, which is why it sits a bit wide in the
right column rather than filling it edge-to-edge.

This same photo (or others like it) would also work well in the Gallery
section, which has been sitting with placeholder color swatches this whole
time waiting for exactly this kind of real material.

That said, the general principle is still worth keeping in mind for
anything added later: a Gallery section showing "the work" needs to be
real photos of Talon's actual clients — stock there would be misleading,
even though stock is fine elsewhere (service icons) when used as
atmosphere rather than a specific claim.

One thing still worth knowing: the three **service icon** photos
(`service-dip-powder.jpg` etc.) are still cropped from the *old* stock
photo, not this new real one — worth revisiting those with real detail
shots once more real photos come in.

## Files (services photos)
- `assets/service-dip-powder.jpg`, `assets/service-gel-manicure.jpg`,
  `assets/service-nail-art.jpg` — close-up crops from the original stock
  hero photo, used as the small icons in the Services list. Worth
  replacing with crops from real photos (like the new hero image) when
  there's time — see the note above.

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
