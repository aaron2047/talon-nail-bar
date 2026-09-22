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
- `assets/gallery-shimmer.jpg`, `assets/gallery-chrome.jpg` — the two real
  Gallery photos currently on the page (gold/black glitter ombre set, deep
  red chrome set). Clean square crops, no feathering, same "keep it real"
  treatment as the hero photo.

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

## About the Gallery
Gallery now shows two real photos instead of the old color-swatch
placeholders: a gold/black glitter ombre set and a deep red chrome set,
both square-cropped, no feathering — same treatment as the hero. The grid
dropped from 6 tiles to 2 on purpose, rather than filling the other 4 with
stock or repeats: a Gallery showing "the work" needs to be real photos of
Talon's actual clients, and a half-empty grid signals unfinished, while
padding it with fakes would undercut the whole "real, not templated" pitch.
Add more real photos as they come in — the grid is a simple 2-column
`repeat(2, 1fr)` in `styles.css`, so a 3rd and 4th photo will slot in
cleanly once you have them (it'll auto-wrap to a second row).

The general principle is still worth keeping in mind for anything else
added later: stock is fine elsewhere (service icons, hero backdrop) when
used as atmosphere, but the Gallery specifically is a claim about Talon's
actual work, so it has to be true photos of it.

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
1. **Gallery** (`#gallery` in index.html) — has 2 real photos now; add more
   as they come in by dropping new image files in `assets/` and adding
   another `<img class="gallery-tile">` line alongside the existing two.
2. **Testimonials** (`#testimonials`) — currently marked
   `[Client testimonial to be added]`. Replace with real quotes once you
   have any — never leave fabricated quotes in their place.
3. **Booking button** — done for the demo. The nav and hero buttons scroll
   to `#book`; the "Check Availability" button there links out to a real,
   working GHL (LeadConnector) booking calendar. See "About the booking
   system" below for how this replaced the earlier Square plan, and what
   changes once Talon signs on.
4. **Footer hours** — currently says "By appointment — message or call to
   confirm times," since we don't have their confirmed weekly hours.
   Update once you know them.
5. **About section copy** — written assuming continuity with the Best of
   Philly 2025 win. If it turns out to be new ownership, rewrite this
   paragraph live with the owner, the same way we planned for the
   GHL-template version.

## About the booking system
Originally set up as a free Square Appointments page, but that plan hit a
wall: Talon already has their own Square account (with booking never
turned on), so putting a second, disconnected Square identity under the
Woolph account would've meant two separate Square presences for one
business — worse than not having booking at all. Since Woolph already
runs the GHL side of this relationship, the calendar moved there instead,
consolidating everything under one roof rather than depending on Square.

Current setup: a **Round Robin** calendar in GHL (LeadConnector), built
inside Talon's sub-account under the Woolph agency account. Round Robin
was picked over "Personal booking" specifically because it scales — a
single placeholder team member today behaves like a shared calendar, and
adding a second stylist later is just adding them to the same rotation,
no rebuild needed. Email confirmations are on for both "Appointment
booked" statuses (Notifications & policies tab on the calendar) — check
there first if a real booking ever doesn't trigger a confirmation email.

The `js-book-link` "Check Availability" button points directly at the
calendar's booking widget URL:
`https://api.leadconnectorhq.com/widget/booking/xzSmQite6T2h0Vf8EKKH`

Once Talon actually signs on:
- Replace the placeholder team member with their real stylist(s).
- Decide whether new bookings should auto-confirm (frictionless, like
  Fresha/Square) or require manual approval first — that's the
  **Booking rules** tab on the calendar, not yet decided either way.
- Confirm the "we will contact you shortly" phone number in the
  confirmation screen is Talon's real number, not Woolph's placeholder.

A separate, bigger idea is on the table: a fully custom booking system
(real backend, no third-party platform at all) as a proprietary
differentiator — "book direct, no fees to anyone else." Genuinely buildable
(Supabase/Cloudflare free tier + email/SMS via Resend/Twilio), and a strong
portfolio piece for Plan B, but it's a multi-day build, not a same-day one
like this. Deliberately sequenced for *after* Talon signs, not before.

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
