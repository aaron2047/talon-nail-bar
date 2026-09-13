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

def leaf_shape(x, y, angle, size, filled=False):
    """A small pointed leaf/petal at (x,y), oriented along `angle`."""
    a = angle
    perp = a + np.pi / 2
    tip_x = x + size * np.cos(a)
    tip_y = y + size * np.sin(a)
    base_x = x - size * 0.25 * np.cos(a)
    base_y = y - size * 0.25 * np.sin(a)
    w = size * 0.34
    c1x = x + w * np.cos(perp) + size * 0.25 * np.cos(a)
    c1y = y + w * np.sin(perp) + size * 0.25 * np.sin(a)
    c2x = x - w * np.cos(perp) + size * 0.25 * np.cos(a)
    c2y = y - w * np.sin(perp) + size * 0.25 * np.sin(a)
    d = (f"M {base_x:.1f} {base_y:.1f} "
         f"Q {c1x:.1f} {c1y:.1f} {tip_x:.1f} {tip_y:.1f} "
         f"Q {c2x:.1f} {c2y:.1f} {base_x:.1f} {base_y:.1f} Z")
    cls = "leaf-fill" if filled else "leaf-outline"
    return f'<path d="{d}" class="{cls}" />'

svg_parts = []
svg_parts.append(
    f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
    f'class="hero-art" preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
)
svg_parts.append('''
<style>
  .tendril { fill: none; stroke: var(--hero-line, #B08D57); stroke-width: 2; stroke-linecap: round; opacity: 0.85; }
  .tendril.soft { stroke: var(--hero-line-soft, #6E5A3E); opacity: 0.5; }
  .leaf-outline { fill: none; stroke: var(--hero-line, #B08D57); stroke-width: 1.6; }
  .leaf-fill { fill: var(--hero-accent, #7A2131); stroke: none; }
  .center-dot { fill: var(--hero-line, #B08D57); opacity: 0.7; }
</style>
''')

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

    # leaves scattered along the tendril, varied count and size
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
        filled = (i == accent_tendril and (frac > 0.85 or (is_last and not accent_placed)))
        if i == accent_tendril and filled:
            accent_placed = True
            size *= 1.25  # make the single accent leaf a touch larger, so it reads as deliberate
        svg_parts.append(leaf_shape(lx, ly, leaf_angle, size, filled=filled))

svg_parts.append(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="4" class="center-dot" />')
svg_parts.append('</svg>')

svg = "\n".join(svg_parts)
with open('/home/claude/talon-nail-bar/assets/hero-art.svg', 'w') as f:
    f.write(svg)

print("Written, length:", len(svg))
