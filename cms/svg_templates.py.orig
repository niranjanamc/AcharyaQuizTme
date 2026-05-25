"""
SVG Diagram Templates for Educational Quiz Questions
=====================================================

This module provides functions that generate clean, well-labeled SVG diagrams
suitable for embedding in JSON-based quiz content. Each function returns a
single-line SVG string with properly quoted XML attributes.

Design System
-------------
- viewBox: 300×200 (landscape) or 300×300 (square)
- Shape stroke: #2563EB (blue), 2px
- Measurement labels: #DC2626 (red), bold, 14–16px
- Highlights: #059669 (green)
- Font: Arial, sans-serif

Usage
-----
    >>> from svg_templates import triangle, svg_to_json_string
    >>> svg = triangle((5, 7, 8), labels=('A', 'B', 'C'))
    >>> json_safe = svg_to_json_string(svg)
"""

from __future__ import annotations

import json
import math
import os
from typing import List, Optional, Sequence, Tuple

# ── Design tokens ────────────────────────────────────────────────────────────
BLUE = "#2563EB"
RED = "#DC2626"
GREEN = "#059669"
FONT = "Arial, sans-serif"
SHAPE_STROKE = 2
GUIDE_STROKE = 1
LABEL_SIZE = 15
MEASUREMENT_SIZE = 14


# ── Helpers ──────────────────────────────────────────────────────────────────

def svg_to_json_string(svg: str) -> str:
    """Escape an SVG string for safe embedding inside a JSON value.

    Uses ``json.dumps`` so all quotes and backslashes are properly escaped.

    Example
    -------
    >>> svg_to_json_string('<svg width="10"></svg>')
    '"<svg width=\\\\"10\\\\"></svg>"'
    """
    return json.dumps(svg)


def _svg_wrap(inner: str, width: int = 300, height: int = 200) -> str:
    """Wrap SVG body in the root <svg> element and return a single-line string."""
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" '
        f'style="background:#fff">'
    )
    # Collapse to a single line
    return (header + inner + "</svg>").replace("\n", " ").replace("  ", " ")


def _text(x: float, y: float, content: str, *,
          color: str = RED, size: int = MEASUREMENT_SIZE,
          bold: bool = True, anchor: str = "middle") -> str:
    weight = "bold" if bold else "normal"
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" '
        f'font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}">{content}</text>'
    )


def _midpoint(x1: float, y1: float, x2: float, y2: float) -> Tuple[float, float]:
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def _offset_label(x1: float, y1: float, x2: float, y2: float,
                  offset: float = 16) -> Tuple[float, float]:
    """Return a point offset perpendicular to the segment (x1,y1)→(x2,y2)."""
    mx, my = _midpoint(x1, y1, x2, y2)
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy) or 1
    nx, ny = -dy / length, dx / length
    return (mx + nx * offset, my + ny * offset)


# ── 1. Triangle ──────────────────────────────────────────────────────────────

def triangle(
    sides: Tuple[float, float, float],
    labels: Optional[Tuple[str, str, str]] = None,
    angles: Optional[Tuple[str, str, str]] = None,
    unit: str = "cm",
) -> str:
    """Draw a triangle with labeled side lengths.

    Parameters
    ----------
    sides : tuple of 3 floats
        Lengths of sides (a=BC, b=AC, c=AB).
    labels : tuple of 3 str, optional
        Vertex labels (default: A, B, C).
    angles : tuple of 3 str, optional
        Angle labels placed near each vertex.
    unit : str
        Unit suffix for side labels (default ``'cm'``).

    Returns
    -------
    str
        Single-line SVG string.

    Example
    -------
    >>> svg = triangle((5, 7, 8), labels=('P', 'Q', 'R'))
    """
    a, b, c = sides
    labels = labels or ("A", "B", "C")

    # Use the law of cosines to compute vertex positions.
    # Place side c (AB) along the bottom.
    # B at origin-ish, A to the right, C above.
    cos_B = (a * a + c * c - b * b) / (2 * a * c) if (2 * a * c) else 0
    cos_B = max(-1, min(1, cos_B))
    sin_B = math.sqrt(max(0, 1 - cos_B * cos_B))

    # Coordinate system: fit into ~260×170 area with padding
    pad = 40
    max_span = 220
    scale = max_span / max(c, a * sin_B + 1e-9, a * cos_B)

    bx, by = pad, 180
    ax, ay = pad + c * scale, 180
    cx, cy = pad + a * cos_B * scale, 180 - a * sin_B * scale

    pts = f"{bx:.1f},{by:.1f} {ax:.1f},{ay:.1f} {cx:.1f},{cy:.1f}"

    body = (
        f'<polygon points="{pts}" fill="none" stroke="{BLUE}" '
        f'stroke-width="{SHAPE_STROKE}" stroke-linejoin="round"/>'
    )

    # Side labels  (sides: a=BC, b=AC, c=AB)
    def _side_label(x1, y1, x2, y2, length, off=16):
        lx, ly = _offset_label(x1, y1, x2, y2, off)
        return _text(lx, ly, f"{length} {unit}".strip())

    body += _side_label(bx, by, ax, ay, c, off=18)   # AB (bottom)
    body += _side_label(ax, ay, cx, cy, b, off=16)    # AC (right)
    body += _side_label(cx, cy, bx, by, a, off=16)    # BC (left)

    # Vertex labels
    offsets_v = [(-12, 10), (12, 10), (0, -10)]
    for i, (vx, vy) in enumerate([(bx, by), (ax, ay), (cx, cy)]):
        ox, oy = offsets_v[i]
        body += _text(vx + ox, vy + oy, labels[i], color=BLUE, size=LABEL_SIZE, bold=True)

    # Angle labels (small text near vertex)
    if angles:
        angle_offsets = [(20, -8), (-20, -8), (0, 18)]
        for i, (vx, vy) in enumerate([(bx, by), (ax, ay), (cx, cy)]):
            if angles[i]:
                ox, oy = angle_offsets[i]
                body += _text(vx + ox, vy + oy, angles[i], color=GREEN, size=12, bold=False)

    return _svg_wrap(body)


# ── 2. Rectangle ─────────────────────────────────────────────────────────────

def rectangle(
    width: float,
    height: float,
    unit: str = "cm",
    labels: Optional[Tuple[str, str, str, str]] = None,
) -> str:
    """Draw a rectangle with width and height labels.

    Parameters
    ----------
    width, height : float
        Logical width and height (used in labels).
    unit : str
        Unit suffix.
    labels : tuple of 4 str, optional
        Vertex labels in order: top-left, top-right, bottom-right, bottom-left.

    Returns
    -------
    str
        Single-line SVG string.

    Example
    -------
    >>> svg = rectangle(12, 5, unit='m', labels=('A','B','C','D'))
    """
    pad = 50
    rw = 200  # rendered width
    rh = 120  # rendered height
    x0, y0 = pad, 30

    body = (
        f'<rect x="{x0}" y="{y0}" width="{rw}" height="{rh}" '
        f'fill="none" stroke="{BLUE}" stroke-width="{SHAPE_STROKE}"/>'
    )

    # Width label (bottom)
    mx = x0 + rw / 2
    body += _text(mx, y0 + rh + 22, f"{width} {unit}".strip())

    # Height label (right)
    body += _text(x0 + rw + 25, y0 + rh / 2 + 5, f"{height} {unit}".strip())

    # Right-angle markers at corners (small squares)
    sq = 10
    for cx, cy in [(x0, y0), (x0 + rw, y0), (x0 + rw, y0 + rh), (x0, y0 + rh)]:
        dx = sq if cx == x0 else -sq
        dy = sq if cy == y0 else -sq
        body += (
            f'<polyline points="{cx + dx:.0f},{cy:.0f} {cx + dx:.0f},{cy + dy:.0f} '
            f'{cx:.0f},{cy + dy:.0f}" fill="none" stroke="{BLUE}" '
            f'stroke-width="1"/>'
        )

    # Vertex labels
    if labels:
        positions = [
            (x0 - 14, y0 - 6),
            (x0 + rw + 14, y0 - 6),
            (x0 + rw + 14, y0 + rh + 16),
            (x0 - 14, y0 + rh + 16),
        ]
        for i, (lx, ly) in enumerate(positions):
            body += _text(lx, ly, labels[i], color=BLUE, size=LABEL_SIZE, bold=True)

    return _svg_wrap(body)


# ── 3. Square ─────────────────────────────────────────────────────────────────

def square(side: float, unit: str = "cm") -> str:
    """Convenience wrapper: draws a square (equal-sided rectangle).

    Parameters
    ----------
    side : float
        Side length for the label.
    unit : str
        Unit suffix.

    Returns
    -------
    str
        Single-line SVG string.

    Example
    -------
    >>> svg = square(9, unit='mm')
    """
    return rectangle(side, side, unit=unit)


# ── 4. Circle ────────────────────────────────────────────────────────────────

def circle(
    radius: float,
    unit: str = "cm",
    show_diameter: bool = False,
) -> str:
    """Draw a circle with a radius line and label.

    Parameters
    ----------
    radius : float
        Radius value for the label.
    unit : str
        Unit suffix.
    show_diameter : bool
        If True, draw the full diameter line and label it as well.

    Returns
    -------
    str
        Single-line SVG string (300×300 viewBox).

    Example
    -------
    >>> svg = circle(7, show_diameter=True)
    """
    cx, cy, r = 150, 150, 100  # rendered circle

    body = (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
        f'stroke="{BLUE}" stroke-width="{SHAPE_STROKE}"/>'
    )

    # Center dot
    body += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{BLUE}"/>'

    if show_diameter:
        # Horizontal diameter line
        body += (
            f'<line x1="{cx - r}" y1="{cy}" x2="{cx + r}" y2="{cy}" '
            f'stroke="{RED}" stroke-width="{GUIDE_STROKE}" stroke-dasharray="5,3"/>'
        )
        body += _text(cx, cy - 10, f"d = {radius * 2} {unit}".strip(), size=13)

    # Radius line (center → right)
    body += (
        f'<line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" '
        f'stroke="{RED}" stroke-width="{SHAPE_STROKE}"/>'
    )
    body += _text(cx + r / 2, cy + 20, f"r = {radius} {unit}".strip())

    # Label "O" at center
    body += _text(cx - 12, cy - 8, "O", color=BLUE, size=LABEL_SIZE, bold=True)

    return _svg_wrap(body, 300, 300)


# ── 5. Number Line ──────────────────────────────────────────────────────────

def number_line(
    start: int,
    end: int,
    step: int = 1,
    highlights: Optional[List[float]] = None,
    unit: str = "",
) -> str:
    """Draw a horizontal number line with tick marks.

    Parameters
    ----------
    start, end : int
        Range of the number line (inclusive).
    step : int
        Interval between tick marks.
    highlights : list of float, optional
        Values to mark with a green dot.
    unit : str
        Optional unit label at the end.

    Returns
    -------
    str
        Single-line SVG string.

    Example
    -------
    >>> svg = number_line(0, 10, step=2, highlights=[3, 7])
    """
    highlights = highlights or []
    pad_x = 30
    line_y = 100
    usable = 240
    span = end - start or 1

    def _xpos(val: float) -> float:
        return pad_x + (val - start) / span * usable

    # Main axis
    body = (
        f'<line x1="{pad_x}" y1="{line_y}" x2="{pad_x + usable}" y2="{line_y}" '
        f'stroke="{BLUE}" stroke-width="{SHAPE_STROKE}"/>'
    )
    # Arrowhead
    ax = pad_x + usable
    body += (
        f'<polygon points="{ax:.0f},{line_y - 5} {ax + 10:.0f},{line_y} '
        f'{ax:.0f},{line_y + 5}" fill="{BLUE}"/>'
    )

    # Ticks and labels
    val = start
    while val <= end:
        x = _xpos(val)
        body += (
            f'<line x1="{x:.1f}" y1="{line_y - 8}" x2="{x:.1f}" y2="{line_y + 8}" '
            f'stroke="{BLUE}" stroke-width="{GUIDE_STROKE}"/>'
        )
        body += _text(x, line_y + 24, str(val), size=13, bold=False)
        val += step

    # Highlights
    for h in highlights:
        hx = _xpos(h)
        body += f'<circle cx="{hx:.1f}" cy="{line_y}" r="5" fill="{GREEN}"/>'
        body += _text(hx, line_y - 14, str(h), color=GREEN, size=13, bold=True)

    # Unit label
    if unit:
        body += _text(pad_x + usable + 20, line_y + 5, unit, color=BLUE, size=12, bold=False)

    return _svg_wrap(body)


# ── 6. Bar Chart ─────────────────────────────────────────────────────────────

def bar_chart(
    data: Sequence[float],
    labels: Sequence[str],
    title: str = "",
    colors: Optional[List[str]] = None,
) -> str:
    """Draw a simple vertical bar chart.

    Parameters
    ----------
    data : list of float
        Bar heights (values).
    labels : list of str
        Category names (same length as *data*).
    title : str, optional
        Chart title.
    colors : list of str, optional
        Per-bar fill colors. Defaults to repeating blue palette.

    Returns
    -------
    str
        Single-line SVG string (300×300 viewBox).

    Example
    -------
    >>> svg = bar_chart([30, 50, 20], ['Mon', 'Tue', 'Wed'], title='Sales')
    """
    n = len(data)
    if not colors:
        palette = [BLUE, "#3B82F6", "#60A5FA", "#93C5FD", "#BFDBFE"]
        colors = [palette[i % len(palette)] for i in range(n)]

    pad_left, pad_right, pad_top, pad_bottom = 45, 15, 40, 50
    chart_w = 300 - pad_left - pad_right
    chart_h = 300 - pad_top - pad_bottom
    max_val = max(data) or 1
    bar_gap = 8
    bar_w = (chart_w - (n + 1) * bar_gap) / n

    body = ""

    # Title
    if title:
        body += _text(150, 24, title, color=BLUE, size=16, bold=True)

    # Y-axis
    body += (
        f'<line x1="{pad_left}" y1="{pad_top}" x2="{pad_left}" '
        f'y2="{pad_top + chart_h}" stroke="{BLUE}" stroke-width="{GUIDE_STROKE}"/>'
    )
    # X-axis
    body += (
        f'<line x1="{pad_left}" y1="{pad_top + chart_h}" '
        f'x2="{pad_left + chart_w}" y2="{pad_top + chart_h}" '
        f'stroke="{BLUE}" stroke-width="{GUIDE_STROKE}"/>'
    )

    # Y-axis ticks (5 ticks)
    for i in range(6):
        val = max_val * i / 5
        y = pad_top + chart_h - (chart_h * i / 5)
        body += (
            f'<line x1="{pad_left - 4}" y1="{y:.1f}" x2="{pad_left}" y2="{y:.1f}" '
            f'stroke="{BLUE}" stroke-width="1"/>'
        )
        body += _text(pad_left - 8, y + 4, f"{val:.0f}", size=10, bold=False, anchor="end")

    # Bars
    for i, (val, lbl) in enumerate(zip(data, labels)):
        bx = pad_left + bar_gap + i * (bar_w + bar_gap)
        bh = (val / max_val) * chart_h
        by = pad_top + chart_h - bh
        body += (
            f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" '
            f'fill="{colors[i]}" rx="2"/>'
        )
        # Value on top
        body += _text(bx + bar_w / 2, by - 5, str(val), size=12, bold=True)
        # Category label
        body += _text(
            bx + bar_w / 2, pad_top + chart_h + 16, lbl,
            color=BLUE, size=11, bold=False,
        )

    return _svg_wrap(body, 300, 300)


# ── 7. Angle Diagram ────────────────────────────────────────────────────────

def angle_diagram(degrees: float, label: str = "") -> str:
    """Draw an angle with an arc showing the degree measurement.

    Parameters
    ----------
    degrees : float
        Angle in degrees (0–360).
    label : str, optional
        Custom label; defaults to ``'{degrees}°'``.

    Returns
    -------
    str
        Single-line SVG string.

    Example
    -------
    >>> svg = angle_diagram(45, label='∠ABC')
    """
    label = label or f"{degrees}°"
    cx, cy = 80, 160       # vertex
    arm_len = 140
    arc_r = 50

    rad = math.radians(degrees)

    # First arm → horizontal right
    ax1, ay1 = cx + arm_len, cy

    # Second arm
    ax2 = cx + arm_len * math.cos(rad)
    ay2 = cy - arm_len * math.sin(rad)

    body = (
        f'<line x1="{cx}" y1="{cy}" x2="{ax1:.1f}" y2="{ay1:.1f}" '
        f'stroke="{BLUE}" stroke-width="{SHAPE_STROKE}"/>'
    )
    body += (
        f'<line x1="{cx}" y1="{cy}" x2="{ax2:.1f}" y2="{ay2:.1f}" '
        f'stroke="{BLUE}" stroke-width="{SHAPE_STROKE}"/>'
    )

    # Arc
    arc_ex = cx + arc_r * math.cos(rad)
    arc_ey = cy - arc_r * math.sin(rad)
    large_arc = 1 if degrees > 180 else 0
    body += (
        f'<path d="M {cx + arc_r:.1f},{cy:.1f} '
        f'A {arc_r} {arc_r} 0 {large_arc} 0 {arc_ex:.1f},{arc_ey:.1f}" '
        f'fill="none" stroke="{RED}" stroke-width="{GUIDE_STROKE}"/>'
    )

    # Label at arc midpoint
    half_rad = rad / 2
    lx = cx + (arc_r + 18) * math.cos(half_rad)
    ly = cy - (arc_r + 18) * math.sin(half_rad)
    body += _text(lx, ly, label, size=14)

    # Vertex dot
    body += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{BLUE}"/>'

    return _svg_wrap(body)


# ── 8. Parallel Lines with Transversal ───────────────────────────────────────

def parallel_lines_with_transversal(angle: float = 60) -> str:
    """Draw two parallel lines cut by a transversal, labeling formed angles.

    Parameters
    ----------
    angle : float
        Angle (in degrees) between the transversal and the horizontal
        parallel lines.

    Returns
    -------
    str
        Single-line SVG string (300×300 viewBox).

    Example
    -------
    >>> svg = parallel_lines_with_transversal(angle=45)
    """
    rad = math.radians(angle)

    # Two horizontal parallel lines
    y1, y2 = 100, 200
    x_start, x_end = 30, 270

    body = ""

    # Parallel line arrows (small chevrons on the right)
    for yy in (y1, y2):
        body += (
            f'<line x1="{x_start}" y1="{yy}" x2="{x_end}" y2="{yy}" '
            f'stroke="{BLUE}" stroke-width="{SHAPE_STROKE}"/>'
        )
        # Arrow marks to indicate parallel
        mx = 230
        body += (
            f'<polyline points="{mx - 5},{yy - 5} {mx},{yy} {mx - 5},{yy + 5}" '
            f'fill="none" stroke="{BLUE}" stroke-width="1.5"/>'
        )
        body += (
            f'<polyline points="{mx - 10},{yy - 5} {mx - 5},{yy} {mx - 10},{yy + 5}" '
            f'fill="none" stroke="{BLUE}" stroke-width="1.5"/>'
        )

    # Transversal: passes through both lines
    mid_x = 150
    # Extend well beyond both lines
    ext = 160
    tx1 = mid_x - ext * math.cos(rad)
    ty1 = y2 + ext * math.sin(rad) * ((y2 - y1) / (2 * ext * math.sin(rad) + 0.01))
    # Actually, let's compute intersection points and extend from there
    # Intersection with line 1 at y1
    ix1 = mid_x
    # Intersection with line 2 at y2
    ix2 = mid_x + (y2 - y1) / math.tan(rad) if math.tan(rad) != 0 else mid_x

    # Extend transversal beyond both intersection points
    dx = math.cos(rad)
    dy = -math.sin(rad)  # SVG y is inverted
    ext_len = 60

    t_x1 = ix1 - dx * ext_len
    t_y1 = y1 + math.sin(rad) * ext_len
    t_x2 = ix2 + dx * ext_len
    t_y2 = y2 - math.sin(rad) * ext_len

    body += (
        f'<line x1="{t_x1:.1f}" y1="{t_y1:.1f}" x2="{t_x2:.1f}" y2="{t_y2:.1f}" '
        f'stroke="{GREEN}" stroke-width="{SHAPE_STROKE}"/>'
    )

    # Label angles at each intersection
    a = angle
    supp = 180 - angle
    # At intersection 1 (upper line)
    body += _text(ix1 + 18, y1 - 8, f"{a}°", color=RED, size=12, bold=True)
    body += _text(ix1 - 22, y1 + 16, f"{supp}°", color=RED, size=12, bold=True)

    # At intersection 2 (lower line)
    body += _text(ix2 + 18, y2 - 8, f"{a}°", color=RED, size=12, bold=True)
    body += _text(ix2 - 22, y2 + 16, f"{supp}°", color=RED, size=12, bold=True)

    # Angle arcs at each intersection
    arc_r = 22
    for ix, iy in [(ix1, y1), (ix2, y2)]:
        arc_ex = ix + arc_r * math.cos(rad)
        arc_ey = iy - arc_r * math.sin(rad)
        body += (
            f'<path d="M {ix + arc_r:.1f},{iy:.1f} '
            f'A {arc_r} {arc_r} 0 0 0 {arc_ex:.1f},{arc_ey:.1f}" '
            f'fill="none" stroke="{RED}" stroke-width="1"/>'
        )

    # Line labels
    body += _text(x_end + 2, y1 - 6, "l₁", color=BLUE, size=14, bold=True, anchor="start")
    body += _text(x_end + 2, y2 - 6, "l₂", color=BLUE, size=14, bold=True, anchor="start")
    body += _text(t_x2 + 4, t_y2 - 6, "t", color=GREEN, size=14, bold=True, anchor="start")

    return _svg_wrap(body, 300, 300)


# ── __main__: generate sample SVGs ──────────────────────────────────────────

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_svgs")
    os.makedirs(out_dir, exist_ok=True)

    samples = {
        "triangle.svg": triangle((5, 7, 8), labels=("A", "B", "C"), angles=("53°", "38°", "89°")),
        "rectangle.svg": rectangle(12, 5, unit="cm", labels=("A", "B", "C", "D")),
        "square.svg": square(9, unit="mm"),
        "circle.svg": circle(7, show_diameter=True),
        "circle_simple.svg": circle(3.5),
        "number_line.svg": number_line(0, 10, step=2, highlights=[3, 7]),
        "bar_chart.svg": bar_chart(
            [30, 50, 20, 45], ["Mon", "Tue", "Wed", "Thu"], title="Daily Sales"
        ),
        "angle_45.svg": angle_diagram(45),
        "angle_90.svg": angle_diagram(90, label="∠ABC = 90°"),
        "angle_120.svg": angle_diagram(120),
        "parallel_60.svg": parallel_lines_with_transversal(60),
        "parallel_45.svg": parallel_lines_with_transversal(45),
    }

    for name, svg_str in samples.items():
        path = os.path.join(out_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg_str)
        print(f"✓ {path}")

    # Demonstrate JSON embedding
    demo = svg_to_json_string(samples["triangle.svg"])
    print(f"\nJSON-safe triangle (first 120 chars):\n{demo[:120]}…")

    print(f"\nAll {len(samples)} sample SVGs saved to {out_dir}/")
