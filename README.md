# Talon Nail Bar — Site Build

A custom-coded site (no template, no site builder) for Talon Nail Bar,
509 S 4th St, Philadelphia, PA 19147.

## Files
- `index.html` — page structure and content
- `styles.css` — all styling
- `script.js` — mobile menu toggle (small, no dependencies)
- `assets/logo.png` — the real logo, used in the header, footer, and favicon
- `assets/talon-logo-mark.svg` — a genuine vector trace of the real logo's
  linework and wordmark (see note below). Not currently used on the page,
  but kept here since it's a clean, scalable asset worth having around —
  e.g. for print materials or a future full-bleed treatment.
- `assets/hero-art.svg` — the hero's visual: original botanical linework
  extending the logo's swirl motif, with small painted-nail shapes (in the
  site's own lacquer colors, with occasional French-tip/dot/moon accents)
  standing in for leaves. Sits in the right column of the two-column hero.
- `generate_hero_art.py` — regenerates `assets/hero-art.svg`. Two separate
  random streams control this: `rng` (the vine/branch geometry — keep this
  seed fixed unless you want a different composition shape) and `paint_rng`
  (which nails get which color/accent detail — change this seed for a
  different color arrangement on the same branch shape). Rerun with
  `python3 generate_hero_art.py` after any edit.

## About the hero graphic
The hero's visual is original artwork, not a stock photo or AI-generated
image — a deliberate choice: a generic photo would raise the same "is this
even real" problem we've been solving for everywhere else on this site,
and AI image generators are especially unreliable at hands and nails,
exactly what a nail salon's own customers look at closest. It started as
plain botanical line art; the small "leaves" were reshaped into painted
nail silhouettes (colored with the site's own lacquer palette, with a few
carrying a small French-tip line, accent dot, or moon-manicure detail) so
it reads unmistakably as nail art rather than generic decoration.

One separate technical note worth keeping in mind: the "herologo.svg" file
you get from Inkscape by just pasting in a screenshot isn't actually
vector — it's a raster image wrapped in SVG markup, so it doesn't scale up
cleanly on its own. `talon-logo-mark.svg` is a proper vectorization of it
(traced with potrace), so it scales to any size without pixelating, if you
ever need a large, crisp version of the logo itself.

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
