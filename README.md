# Talon Nail Bar — Site Build

A custom-coded site (no template, no site builder) for Talon Nail Bar,
509 S 4th St, Philadelphia, PA 19147.

## Files
- `index.html` — page structure and content
- `styles.css` — all styling
- `script.js` — mobile menu toggle (small, no dependencies)
- `assets/` — logo, hero art, ready for real photos once you have them
- `generate_hero_art.py` — regenerates `assets/hero-art.svg` if you ever want
  a different variation of the hero linework. Change the `rng = np.random.default_rng(23)`
  seed number to get a different composition, then rerun with `python3 generate_hero_art.py`.

## About the hero graphic
The hero's visual is an original SVG — a botanical linework piece extending
the swirl motif from the real logo, not a stock photo or AI-generated image.
This was a deliberate choice: a generic stock/AI photo of a hand would raise
the same "is this even real" problem we've been solving for everywhere else
on this site, and AI image generators are especially unreliable at rendering
hands and nails correctly — exactly the one detail nail salon visitors look
at closest. The linework bleeds off the right edge of the hero for scale and
impact — this depends on the two-column grid layout, which this project's
own preview tooling can't render (see note below), so check this section
specifically in a real browser once deployed.

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

## Deploying (same pattern as BullForce Powerwash)
1. Create a new GitHub repo (e.g. `talon-nail-bar`) under your account.
2. From this folder: `git init`, `git add .`, `git commit -m "Initial build"`,
   then follow GitHub's instructions to push to the new repo.
3. In Netlify, "Add new site" → "Import an existing project" → connect the
   GitHub repo → deploy. No build settings needed, this is plain HTML/CSS/JS.
4. Once live, connect the domain (or use the free Netlify subdomain for
   the demo/pitch, and a real domain later if they sign on).

## Notes on the design
- Colors, type, and layout choices are written up in the CSS file comments
  and match the brand's existing black-and-white identity from their
  Instagram.
- Built mobile-responsive, with keyboard focus states and reduced-motion
  support out of the box.
- No external dependencies beyond Google Fonts (Fraunces + Work Sans),
  loaded directly in `index.html`.
