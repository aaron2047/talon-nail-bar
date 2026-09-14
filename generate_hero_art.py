import numpy as np

# ------------------------------------------------------------------
# Generates a radial botanical linework composition (tendrils curling
# outward from a shared center, each ending in a small leaf), echoing
# the swirl motif in the real Talon Nail Bar logo, at hero-graphic scale.
# ------------------------------------------------------------------

W, H = 640, 760
CX, CY = W * 0.38, H * 0.58

N_TENDRILS = 9
rng = np.random.default_rng(23)
# Separate stream for color/style decisions, so adding these choices doesn't
# shift the geometry random draws and change the approved composition.
paint_rng = np.random.default_rng(23)

def spiral_points(angle0, length, curl, n=40):
    """Generate points for one tendril curling outward from center."""
    t = np.linspace(0, 1, n)
    r = length * (0.12 + 0.88 * t**1.3)
    # curl eases off rather than completing full loops, for a looser, less mandala-like feel
    theta = angle0 + curl * (1 - np.exp(-2.2 * t))
    wobble = 0.06 * np.sin(t * rng.uniform(3, 6) * np.pi + rng.uniform(0, 6))
    x = CX + r * np.cos(theta + wobble)
    y = CY + r * np.sin(theta + wobble) * 1.08
    return x, y

def catmull_rom_to_bezier(xs, ys):
    """Convert a point sequence into a smooth SVG path (cubic beziers)."""
    pts = list(zip(xs, ys))
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f} "
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1 = pts[i]
        p2 = pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else pts[i + 1]
        c1x = p1[0] + (p2[0] - p0[0]) / 6
        c1y = p1[1] + (p2[1] - p0[1]) / 6
        c2x = p2[0] - (p3[0] - p1[0]) / 6
        c2y = p2[1] - (p3[1] - p1[1]) / 6
        d += f"C {c1x:.1f} {c1y:.1f} {c2x:.1f} {c2y:.1f} {p2[0]:.1f} {p2[1]:.1f} "
    return d.strip()

def nail_shape(x, y, angle, size, color, style='plain'):
    """A small painted-nail silhouette at (x,y), oriented along `angle`.
    Rounder at the tip than a leaf point, filled with a lacquer color,
    with an optional small nail-art detail (tip line / dot / moon)."""
    a = angle
    perp = a + np.pi / 2
    tip_x = x + size * np.cos(a)
    tip_y = y + size * np.sin(a)
    base_x = x - size * 0.22 * np.cos(a)
    base_y = y - size * 0.22 * np.sin(a)
    w = size * 0.48
    # control points pulled further toward the tip than a leaf point,
    # so the curve rounds off rather than coming to a sharp point —
    # reads as an almond nail shape rather than a petal
    c1x = x + w * np.cos(perp) + size * 0.45 * np.cos(a)
    c1y = y + w * np.sin(perp) + size * 0.45 * np.sin(a)
    c2x = x - w * np.cos(perp) + size * 0.45 * np.cos(a)
    c2y = y - w * np.sin(perp) + size * 0.45 * np.sin(a)
    d = (f"M {base_x:.1f} {base_y:.1f} "
         f"Q {c1x:.1f} {c1y:.1f} {tip_x:.1f} {tip_y:.1f} "
         f"Q {c2x:.1f} {c2y:.1f} {base_x:.1f} {base_y:.1f} Z")
    parts = [f'<path d="{d}" fill="{color}" class="nail-shape" />']

    if style == 'tip':
        # a thin pale line near the tip — French-tip suggestion
        lt_x = x + size * 0.74 * np.cos(a)
        lt_y = y + size * 0.74 * np.sin(a)
        l1x = lt_x + w * 0.75 * np.cos(perp)
        l1y = lt_y + w * 0.75 * np.sin(perp)
        l2x = lt_x - w * 0.75 * np.cos(perp)
        l2y = lt_y - w * 0.75 * np.sin(perp)
        parts.append(
            f'<path d="M {l1x:.1f} {l1y:.1f} Q {tip_x:.1f} {tip_y:.1f} {l2x:.1f} {l2y:.1f}" '
            f'class="nail-detail-line" />'
        )
    elif style == 'dot':
        # a single small accent dot — echoes the metallic-microdot trend
        dot_x = x + size * 0.3 * np.cos(a)
        dot_y = y + size * 0.3 * np.sin(a)
        parts.append(f'<circle cx="{dot_x:.1f}" cy="{dot_y:.1f}" r="{max(size*0.07,1.6):.1f}" class="nail-detail-dot" />')
    elif style == 'moon':
        # a pale crescent near the cuticle end — moon-manicure suggestion
        moon_x = base_x + size * 0.14 * np.cos(a)
        moon_y = base_y + size * 0.14 * np.sin(a)
        parts.append(f'<circle cx="{moon_x:.1f}" cy="{moon_y:.1f}" r="{max(size*0.1,1.8):.1f}" class="nail-detail-moon" />')

    return "\n".join(parts)

svg_parts = []
svg_parts.append(
    f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
    f'class="hero-art" preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
)
svg_parts.append('''
<style>
  .tendril { fill: none; stroke: var(--hero-line, #B08D57); stroke-width: 2; stroke-linecap: round; opacity: 0.85; }
  .tendril.soft { stroke: var(--hero-line-soft, #6E5A3E); opacity: 0.5; }
  .nail-shape { stroke: #14110F; stroke-width: 1; opacity: 0.96; }
  .nail-detail-line { fill: none; stroke: #F2ECE3; stroke-width: 1.4; opacity: 0.8; }
  .nail-detail-dot { fill: #F2ECE3; opacity: 0.85; }
  .nail-detail-moon { fill: #F2ECE3; opacity: 0.75; }
  .center-dot { fill: var(--hero-line, #B08D57); opacity: 0.7; }
</style>
''')

# The site's own lacquer palette (matches assets used elsewhere on the page) —
# using the same colors here keeps this graphic visually tied to the rest
# of the site rather than introducing a new, separate palette.
POLISH_COLORS = ["#7A2131", "#C97B76", "#4B2138", "#C9A66B", "#3B1220", "#E3C9B0"]
ACCENT_COLOR = "#7A2131"

accent_tendril = rng.integers(0, N_TENDRILS)

for i in range(N_TENDRILS):
    # bias angles toward the upper-right (growing outward/upward) rather than full 360 symmetry
    angle0 = rng.uniform(-1.9, 0.5) + rng.uniform(-0.15, 0.15)
    length = rng.uniform(260, 420)
    curl = rng.uniform(0.9, 2.6) * (1 if rng.random() > 0.35 else -1)
    xs, ys = spiral_points(angle0, length, curl)
    is_soft = rng.random() < 0.4 and i != accent_tendril
    cls = "tendril soft" if is_soft else "tendril"
    path_d = catmull_rom_to_bezier(xs, ys)
    svg_parts.append(f'<path d="{path_d}" class="{cls}" />')

    # painted nails scattered along the tendril, varied count, color, and size
    n_leaves = rng.integers(2, 4)
    accent_placed = False
    for leaf_i in range(n_leaves):
        frac = rng.uniform(0.35, 0.95)
        idx = int(frac * (len(xs) - 1))
        lx, ly = xs[idx], ys[idx]
        idx2 = min(idx + 1, len(xs) - 1)
        tangent = np.arctan2(ys[idx2] - ly, xs[idx2] - lx)
        leaf_angle = tangent + rng.choice([-1, 1]) * rng.uniform(1.0, 1.7)
        size = rng.uniform(16, 30) * (1.3 if frac > 0.85 else 1.0)
        is_last = leaf_i == n_leaves - 1
        is_accent = (i == accent_tendril and (frac > 0.85 or (is_last and not accent_placed)))

        if is_accent:
            accent_placed = True
            size *= 1.3  # the single deliberate accent nail, a touch larger
            color = ACCENT_COLOR
            style = paint_rng.choice(['dot', 'moon'])
        else:
            color = paint_rng.choice(POLISH_COLORS)
            # most nails stay plain for a clean, uncluttered read; a minority
            # get a small design detail so it doesn't turn busy
            style = paint_rng.choice(['plain', 'plain', 'plain', 'tip', 'dot', 'moon'])

        svg_parts.append(nail_shape(lx, ly, leaf_angle, size, color, style=style))

svg_parts.append(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="4" class="center-dot" />')
svg_parts.append('</svg>')

svg = "\n".join(svg_parts)
with open('/home/claude/talon-nail-bar/assets/hero-art.svg', 'w') as f:
    f.write(svg)

print("Written, length:", len(svg))
