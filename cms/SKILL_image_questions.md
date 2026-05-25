# SKILL: Image-Based Question Generation

> **Audience**: AI agents and human content creators generating quiz questions for the Bhagiratha Quiz app.
> **Last Updated**: 2026-05-25

---

## Table of Contents

1. [Overview](#1-overview)
2. [JSON Schema Reference](#2-json-schema-reference)
3. [SVG Diagram Guidelines](#3-svg-diagram-guidelines)
4. [Raster Image Guidelines](#4-raster-image-guidelines)
5. [Subject-Specific Guidance](#5-subject-specific-guidance)
6. [Quality Checklist](#6-quality-checklist)
7. [Content Generation Prompt Template](#7-content-generation-prompt-template)
8. [Validation](#8-validation)

---

## 1. Overview

### What Are Image-Based Questions?

Image-based questions present a visual element — a diagram, photograph, chart, or illustration — as the primary stimulus. The student must **interpret the image** to answer the question. These questions are critical because they:

- **Test deeper understanding**: reading a shape's measurement from a diagram is harder than recalling a formula.
- **Engage visual learners**: many concepts in math, science, and geography are inherently visual.
- **Mirror textbook pedagogy**: NCERT textbooks (Math-Magic, Ganita Prakash, Curiosity) rely heavily on diagrams.
- **Support lower-grade students**: Classes 1–3 depend on pictures for counting, pattern, and letter recognition.

### Two Rendering Strategies

| Strategy | Best For | Stored As | Rendered By |
|---|---|---|---|
| **Inline SVG** (preferred) | Geometric diagrams, number lines, charts, circuit diagrams, coordinate planes, graph paper patterns | `image.svg` field containing a complete `<svg>` string | React's `dangerouslySetInnerHTML` or direct JSX embedding |
| **Raster Image** | Photographs of monuments, animals, maps, lab apparatus, real-world objects | `image.src` field pointing to a file in `public/images/questions/` | Standard `<img>` tag |

> **Rule of thumb**: If you can _draw_ it with lines, arcs, and text, use SVG. If it's a _photograph_ of a real thing, use a raster image.

---

## 2. JSON Schema Reference

### Existing Question Types (Context)

The app currently supports three question types: `single`, `multiple`, and `match`. Image questions introduce two new types that extend the existing pattern:

- `image_single` — an image plus single-choice options
- `image_multiple` — an image plus multiple-choice options (select all that apply)

### 2.1 `image_single` Schema

```json
{
  "id": "<prefix>_img_<NNN>",
  "type": "image_single",
  "difficulty": 1,
  "image": {
    "type": "svg",
    "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'>...</svg>",
    "alt": {
      "en": "A triangle with sides labelled 5 cm, 7 cm, and 9 cm",
      "kn": "5 ಸೆಂ.ಮೀ., 7 ಸೆಂ.ಮೀ. ಮತ್ತು 9 ಸೆಂ.ಮೀ. ಬಾಹುಗಳಿರುವ ತ್ರಿಕೋನ"
    }
  },
  "en": {
    "question": "What is the perimeter of this triangle?",
    "options": ["15 cm", "21 cm", "35 cm", "12 cm"],
    "answer": "21 cm",
    "reasoning": "The perimeter is the sum of all sides: 5 + 7 + 9 = 21 cm."
  },
  "kn": {
    "question": "ಈ ತ್ರಿಕೋನದ ಸುತ್ತಳತೆ ಎಷ್ಟು?",
    "options": ["15 ಸೆಂ.ಮೀ.", "21 ಸೆಂ.ಮೀ.", "35 ಸೆಂ.ಮೀ.", "12 ಸೆಂ.ಮೀ."],
    "answer": "21 ಸೆಂ.ಮೀ.",
    "reasoning": "ಸುತ್ತಳತೆ ಎಂದರೆ ಎಲ್ಲಾ ಬಾಹುಗಳ ಮೊತ್ತ: 5 + 7 + 9 = 21 ಸೆಂ.ಮೀ."
  }
}
```

### 2.2 `image_multiple` Schema

```json
{
  "id": "<prefix>_img_<NNN>",
  "type": "image_multiple",
  "difficulty": 2,
  "image": {
    "type": "svg",
    "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'>...</svg>",
    "alt": {
      "en": "A shape made of two rectangles joined at one side",
      "kn": "ಒಂದು ಬದಿಯಲ್ಲಿ ಜೋಡಿಸಿದ ಎರಡು ಆಯತಗಳಿಂದ ಮಾಡಿದ ಆಕಾರ"
    }
  },
  "en": {
    "question": "Which of the following are true about this shape?",
    "options": [
      "It has exactly 6 sides",
      "It has 4 right angles",
      "It has 8 right angles",
      "It is made of 2 rectangles"
    ],
    "answer": ["It has exactly 6 sides", "It has 8 right angles", "It is made of 2 rectangles"],
    "reasoning": "The L-shape is composed of two rectangles. It has 6 outer sides and 8 right angles (4 from each rectangle, with 2 shared)."
  },
  "kn": {
    "question": "ಈ ಆಕಾರದ ಬಗ್ಗೆ ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಿ?",
    "options": [
      "ಇದಕ್ಕೆ ನಿಖರವಾಗಿ 6 ಬಾಹುಗಳಿವೆ",
      "ಇದಕ್ಕೆ 4 ಲಂಬ ಕೋನಗಳಿವೆ",
      "ಇದಕ್ಕೆ 8 ಲಂಬ ಕೋನಗಳಿವೆ",
      "ಇದು 2 ಆಯತಗಳಿಂದ ಮಾಡಲ್ಪಟ್ಟಿದೆ"
    ],
    "answer": ["ಇದಕ್ಕೆ ನಿಖರವಾಗಿ 6 ಬಾಹುಗಳಿವೆ", "ಇದಕ್ಕೆ 8 ಲಂಬ ಕೋನಗಳಿವೆ", "ಇದು 2 ಆಯತಗಳಿಂದ ಮಾಡಲ್ಪಟ್ಟಿದೆ"],
    "reasoning": "L-ಆಕಾರವು ಎರಡು ಆಯತಗಳಿಂದ ಕೂಡಿದೆ. ಇದು 6 ಹೊರಗಿನ ಬಾಹುಗಳನ್ನು ಮತ್ತು 8 ಲಂಬ ಕೋನಗಳನ್ನು ಹೊಂದಿದೆ."
  }
}
```

### 2.3 Options with Images

When options need images, they should be objects containing an `id` and `image`. The `text` field is optional. The `answer` array/string will reference the option `id`s.

```json
{
  "id": "c5_math_shapes_img_001",
  "type": "image_single",
  "difficulty": 1,
  "en": {
    "question": "Which shape has exactly 4 equal sides?",
    "options": [
      { "id": "optA", "text": "Shape A", "image": { "type": "svg", "svg": "<svg>...</svg>" } },
      { "id": "optB", "text": "Shape B", "image": { "type": "svg", "svg": "<svg>...</svg>" } }
    ],
    "answer": "optA",
    "reasoning": "A square has 4 equal sides"
  },
  "kn": {
    "question": "ಯಾವ ಆಕಾರವು 4 ಸಮಾನ ಬದಿಗಳನ್ನು ಹೊಂದಿದೆ?",
    "options": [
      { "id": "optA", "text": "ಆಕಾರ A", "image": { "type": "svg", "svg": "<svg>...</svg>" } },
      { "id": "optB", "text": "ಆಕಾರ B", "image": { "type": "svg", "svg": "<svg>...</svg>" } }
    ],
    "answer": "optA",
    "reasoning": "ಚೌಕವು 4 ಸಮಾನ ಬದಿಗಳನ್ನು ಹೊಂದಿದೆ"
  }
}
```

### 2.4 Raster Image Variant

When using a photograph instead of an SVG diagram, replace the `image` object:

```json
{
  "id": "c5_his_mon_img_001",
  "type": "image_single",
  "difficulty": 1,
  "image": {
    "type": "raster",
    "src": "class_5/history/monuments_001.webp",
    "alt": {
      "en": "Photograph of the India Gate in New Delhi",
      "kn": "ನವದೆಹಲಿಯಲ್ಲಿರುವ ಇಂಡಿಯಾ ಗೇಟ್‌ನ ಫೋಟೋ"
    }
  },
  "en": {
    "question": "Which famous monument is shown in this photograph?",
    "options": ["Gateway of India", "India Gate", "Qutub Minar", "Red Fort"],
    "answer": "India Gate",
    "reasoning": "The photograph shows India Gate, a war memorial located in New Delhi, built in 1931 to honour Indian soldiers who died in World War I."
  },
  "kn": {
    "question": "ಈ ಫೋಟೋದಲ್ಲಿ ಯಾವ ಪ್ರಸಿದ್ಧ ಸ್ಮಾರಕವನ್ನು ತೋರಿಸಲಾಗಿದೆ?",
    "options": ["ಗೇಟ್‌ವೇ ಆಫ್ ಇಂಡಿಯಾ", "ಇಂಡಿಯಾ ಗೇಟ್", "ಕುತುಬ್ ಮಿನಾರ್", "ಕೆಂಪು ಕೋಟೆ"],
    "answer": "ಇಂಡಿಯಾ ಗೇಟ್",
    "reasoning": "ಈ ಫೋಟೋ ಇಂಡಿಯಾ ಗೇಟ್ ಅನ್ನು ತೋರಿಸುತ್ತದೆ, ಇದು ನವದೆಹಲಿಯಲ್ಲಿರುವ ಯುದ್ಧ ಸ್ಮಾರಕವಾಗಿದೆ."
  }
}
```

### 2.4 Field Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | ✅ | Unique ID. Format: `<prefix>_img_<NNN>`. Example: `c5_mat_sa_img_001` |
| `type` | string | ✅ | Must be `"image_single"` or `"image_multiple"` |
| `difficulty` | integer | ✅ | `1` (easy), `2` (medium), or `3` (hard) |
| `image` | object | ✅ | The image payload (see below) |
| `image.type` | string | ✅ | `"svg"` or `"raster"` |
| `image.svg` | string | ✅ (if svg) | Complete, valid SVG XML string |
| `image.src` | string | ✅ (if raster) | Relative path from `public/images/questions/` |
| `image.alt` | object | ✅ | Alt text in `{ "en": "...", "kn": "..." }` format |
| `en` | object | ✅ | English question content |
| `kn` | object | ✅ | Kannada question content |
| `en.question` | string | ✅ | The question text |
| `en.options` | array | ✅ | 4 answer choices (strings or objects with id/image) |
| `en.answer` | string or array | ✅ | Correct answer(s). String/ID for `image_single`, array of strings/IDs for `image_multiple` |
| `en.reasoning` | string | ✅ | Explanation shown after answering |

> **ID Prefix Convention**: Follow the existing pattern from the codebase. Examples:
> - Class 5, Maths, Shapes & Angles: `c5_mat_sa_img_001`
> - Class 6, Science, Electricity: `c6_sci_ec_img_001`
> - General, GK, Indian Heritage: `gen_gk_ih_img_001`
> - Always zero-pad to 3 digits: `_img_001`, `_img_002`, ..., `_img_099`

---

## 3. SVG Diagram Guidelines

### 3.1 Canvas & Viewport

| Property | Value | Notes |
|---|---|---|
| **viewBox (landscape)** | `0 0 300 200` | Use for wide diagrams: number lines, rectangles, bar charts |
| **viewBox (square)** | `0 0 300 300` | Use for circles, coordinate planes, square shapes |
| **xmlns** | `http://www.w3.org/2000/svg` | Always include for valid standalone SVG |
| **Background** | `transparent` (default) | The app container has a white/light background |

### 3.2 Color Palette

Use these exact hex codes for consistency across all diagrams:

| Purpose | Color | Hex | Preview |
|---|---|---|---|
| **Primary shapes** (lines, borders) | Blue | `#2563EB` | 🔵 |
| **Measurements & labels** | Red | `#DC2626` | 🔴 |
| **Highlights & fills** | Green | `#059669` | 🟢 |
| **Light fill** (area shading) | Light Blue | `#DBEAFE` | ⬜ |
| **Angle arcs** | Orange | `#EA580C` | 🟠 |
| **Grid lines** | Light Gray | `#E5E7EB` | ⬜ |
| **Text** | Dark Gray | `#1F2937` | ⬛ |

### 3.3 Typography

- **Font family**: `Arial, sans-serif` (universally available)
- **Label size**: `14px` for measurements, `12px` for axis labels
- **Title size**: `16px` (bold) if a diagram title is needed
- **Kannada text in SVG**: Do **not** embed Kannada in SVG labels. The question text and options handle Kannada. SVG labels should use English/numeric values only (e.g., "5 cm", "A", "B").
- **text-anchor**: Use `middle` for centered labels, `start`/`end` for edge-aligned

### 3.4 Stroke & Fill Rules

```
stroke-width: 2        (shape outlines)
stroke-width: 1        (grid lines, helper lines)
stroke-linecap: round  (for line segments)
fill: none              (default for shapes, unless shading area)
```

### 3.5 SVG Templates Module

The file `cms/svg_templates.py` (to be created) provides Python helper functions for generating common SVG patterns. Use these when batch-generating questions:

```python
# cms/svg_templates.py — reference API

def triangle_with_sides(a, b, c, labels=None):
    """Generate SVG of a triangle with labeled side lengths.
    
    Args:
        a, b, c: side lengths (used for label text)
        labels: optional dict {"a": "5 cm", "b": "7 cm", "c": "9 cm"}
    Returns:
        Complete SVG string
    """

def rectangle_with_dimensions(width, height, label_w="", label_h=""):
    """Generate SVG of a rectangle with width and height labels."""

def number_line(start, end, step=1, highlights=None):
    """Generate SVG of a number line.
    
    Args:
        start, end: range of the number line
        step: interval between tick marks
        highlights: list of values to mark with a colored dot
    Returns:
        Complete SVG string
    """

def circle_with_radius(radius, show_diameter=False):
    """Generate SVG of a circle with radius/diameter labeled."""

def coordinate_plane(x_range, y_range, points=None):
    """Generate SVG of a 2D coordinate plane with plotted points."""

def bar_chart(data, labels, title=""):
    """Generate SVG bar chart from data."""

def angle_diagram(degrees, label=""):
    """Generate SVG showing an angle with arc and degree label."""
```

### 3.6 Complete SVG Examples

#### Example 1: Triangle with Labeled Sides

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <!-- Triangle shape -->
  <polygon
    points="150,20 30,170 270,170"
    fill="none"
    stroke="#2563EB"
    stroke-width="2"
    stroke-linejoin="round"
  />
  <!-- Side labels in red -->
  <text x="80" y="90" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" transform="rotate(-55, 80, 90)">7 cm</text>
  <text x="220" y="90" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" transform="rotate(55, 220, 90)">5 cm</text>
  <text x="150" y="192" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">9 cm</text>
  <!-- Vertex labels -->
  <text x="150" y="15" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" font-weight="bold">A</text>
  <text x="22" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" font-weight="bold">B</text>
  <text x="278" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" font-weight="bold">C</text>
</svg>
```

#### Example 2: Rectangle with Dimensions

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <!-- Rectangle -->
  <rect x="40" y="30" width="220" height="120" fill="#DBEAFE" stroke="#2563EB" stroke-width="2" rx="2"/>
  <!-- Width label (top) -->
  <line x1="40" y1="20" x2="260" y2="20" stroke="#DC2626" stroke-width="1" marker-start="url(#arrowL)" marker-end="url(#arrowR)"/>
  <text x="150" y="15" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">12 cm</text>
  <!-- Height label (right) -->
  <line x1="270" y1="30" x2="270" y2="150" stroke="#DC2626" stroke-width="1"/>
  <text x="285" y="95" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" transform="rotate(90, 285, 95)">8 cm</text>
  <!-- Right-angle markers -->
  <path d="M40,30 L55,30 L55,45" fill="none" stroke="#EA580C" stroke-width="1.5"/>
  <path d="M260,30 L245,30 L245,45" fill="none" stroke="#EA580C" stroke-width="1.5"/>
  <path d="M40,150 L55,150 L55,135" fill="none" stroke="#EA580C" stroke-width="1.5"/>
  <path d="M260,150 L245,150 L245,135" fill="none" stroke="#EA580C" stroke-width="1.5"/>
  <!-- Arrow markers (define once) -->
  <defs>
    <marker id="arrowL" markerWidth="8" markerHeight="8" refX="0" refY="4" orient="auto">
      <path d="M8,0 L0,4 L8,8" fill="none" stroke="#DC2626" stroke-width="1"/>
    </marker>
    <marker id="arrowR" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8" fill="none" stroke="#DC2626" stroke-width="1"/>
    </marker>
  </defs>
</svg>
```

#### Example 3: Number Line

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 100">
  <!-- Main line -->
  <line x1="20" y1="50" x2="280" y2="50" stroke="#2563EB" stroke-width="2" stroke-linecap="round"/>
  <!-- Arrow at right end -->
  <polygon points="280,50 272,44 272,56" fill="#2563EB"/>
  <!-- Tick marks and labels for 0 through 10 -->
  <line x1="30" y1="40" x2="30" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="30" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">0</text>
  <line x1="55" y1="40" x2="55" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="55" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">1</text>
  <line x1="80" y1="40" x2="80" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="80" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">2</text>
  <line x1="105" y1="40" x2="105" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="105" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">3</text>
  <line x1="130" y1="40" x2="130" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="130" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">4</text>
  <line x1="155" y1="40" x2="155" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="155" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">5</text>
  <line x1="180" y1="40" x2="180" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="180" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">6</text>
  <line x1="205" y1="40" x2="205" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="205" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">7</text>
  <line x1="230" y1="40" x2="230" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="230" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">8</text>
  <line x1="255" y1="40" x2="255" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="255" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">9</text>
  <!-- Highlighted point at 3 -->
  <circle cx="105" cy="50" r="6" fill="#059669" stroke="white" stroke-width="2"/>
  <!-- Question mark at unknown position -->
  <circle cx="205" cy="50" r="6" fill="#DC2626" stroke="white" stroke-width="2"/>
  <text x="205" y="30" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" font-weight="bold">?</text>
</svg>
```

---

## 4. Raster Image Guidelines

### 4.1 Image Specifications

| Property | Requirement |
|---|---|
| **Preferred format** | WebP (best compression for photos), GIF (for simple animations) |
| **Fallback format** | PNG (for transparency or when WebP isn't available) |
| **Maximum file size** | 100 KB per image |
| **Maximum dimensions** | 600 × 400 px (landscape), 400 × 400 px (square) |
| **Minimum dimensions** | 300 × 200 px |
| **Color space** | sRGB |
| **DPI** | 72 (screen resolution) |

### 4.2 Storage Path Convention

All raster images MUST be stored under:

```
public/images/questions/{classId}/{subjectId}/{chapterId}_{NNN}.webp
```

**Examples:**

```
public/images/questions/class_5/history/monuments_001.webp
public/images/questions/class_5/history/monuments_002.webp
public/images/questions/class_6/science/electricity_circuits_001.webp
public/images/questions/general/gk/indian_heritage_001.webp
```

**Naming rules:**

- Use the `chapterId` from `catalog.json` as the prefix
- Append a 3-digit zero-padded index: `_001`, `_002`, ..., `_999`
- All lowercase, underscores only (no spaces, no hyphens)
- Extension: `.webp` (preferred) or `.png`

### 4.3 The `image.src` Path

The `src` field in the JSON is a **relative path** from `public/images/questions/`. Do NOT include `public/images/questions/` in the src value.

```json
// ✅ Correct
"src": "class_5/history/monuments_001.webp"

// ❌ Wrong — do NOT include the base directory
"src": "public/images/questions/class_5/history/monuments_001.webp"

// ❌ Wrong — do NOT use absolute paths
"src": "/Users/murthy/project/public/images/questions/class_5/history/monuments_001.webp"
```

### 4.4 Image Sourcing

- **Photographs**: Use only royalty-free, Creative Commons (CC0/CC-BY), or self-created images.
- **Attribution**: If CC-BY, include an `attribution` field in the `image` object:
  ```json
  "image": {
    "type": "raster",
    "src": "class_5/history/monuments_001.webp",
    "alt": { "en": "...", "kn": "..." },
    "attribution": "Photo by Wikimedia Commons, CC BY-SA 4.0"
  }
  ```
- **No copyrighted textbook scans**: Never scan and include images from NCERT textbooks directly.

### 4.5 Image Optimization Commands

```bash
# Convert to WebP with quality 80 (good balance of quality and size)
cwebp -q 80 input.png -o output.webp

# Resize to max 600x400, maintaining aspect ratio
magick input.jpg -resize 600x400\> -quality 80 output.webp

# Check file size (must be < 100KB)
ls -la output.webp
```

---

## 5. Subject-Specific Guidance

### 5.1 Mathematics

Mathematics benefits the most from image questions. Prioritize inline SVG for all diagrams.

| Chapter / Topic | Diagram Types | Difficulty Spread |
|---|---|---|
| **Shapes & Angles** | Triangles with labeled angles, angle comparison, right-angle markers | D1: identify shape → D3: calculate missing angle |
| **How Many Squares** | Grid-based counting diagrams, overlapping squares | D1: simple grid → D3: nested squares |
| **Parts & Wholes** | Fraction circles, shaded bars, pizza/pie slices | D1: identify fraction → D3: compare/add fractions |
| **Patterns** | Repeating shape sequences, growing patterns | D1: next in sequence → D3: find the rule |
| **Area & Boundary** | Rectangles/L-shapes with dimensions, grid-counting | D1: count grid squares → D3: composite shapes |
| **Lines & Angles** (Class 6) | Intersecting lines, parallel lines with transversal, angle pairs | D2–D3 |
| **Perimeter & Area** (Class 6) | Complex shapes with dimensions, area comparison | D2–D3 |
| **Symmetry** (Class 6) | Mirror lines, symmetrical shape completion | D1–D2 |
| **The Other Side of Zero** (Class 6) | Number lines with negative numbers | D1–D3 |

**SVG tips for math:**
- Always show right-angle markers (small squares) using `<path>` elements
- Use `<text>` with `transform="rotate()"` for labels on angled sides
- For grid/graph paper, use `<pattern>` to create repeating grid lines

### 5.2 Science

| Topic | Diagram Types | Notes |
|---|---|---|
| **Electricity & Circuits** | Simple circuit diagrams (battery, bulb, switch, wires) | Use SVG. Standard symbols: battery (two lines), bulb (circle with X), switch (gap) |
| **Getting to Know Plants** | Labeled diagram of plant parts (root, stem, leaf, flower) | SVG preferred. Simple line drawings work well |
| **Body Movements** | Joint types, skeleton outline | SVG for simple joints; raster for detailed anatomy |
| **Light, Shadows & Reflections** | Shadow formation, mirror reflection diagrams | SVG with dashed lines for light rays |
| **Food Components** | Nutrient chart, food group classification | SVG bar charts or pie charts |
| **Magnets** | Magnetic field lines, attraction/repulsion | SVG with curved lines and N/S labels |
| **From Tasting to Digesting** (EVS) | Digestive system outline | SVG for simple; raster for detailed |
| **Experiments with Water** (EVS) | Lab apparatus: beaker, funnel, filter paper | SVG preferred |

**SVG tips for science:**
- Use dashed strokes (`stroke-dasharray="5,3"`) for invisible forces, light rays, magnetic fields
- Arrow markers for direction of current, light, food chain flow
- Use `<circle>` with labels for atoms in basic molecule diagrams

### 5.3 History / Geography

| Topic | Diagram Types | Image Source |
|---|---|---|
| **Historical Timelines** | Timeline SVG with labeled events | SVG (inline) |
| **The Indus Valley Civilization** | Map of Indus sites, seal images | Raster (maps, artifact photos) |
| **Ancient Empires** | Empire boundary maps | Raster (historical maps) |
| **Freedom Movement** | Photos of leaders, event timelines | Raster (historical photos) |
| **Historic Forts & Monuments** | Photos of monuments | Raster (architectural photos) |
| **Maps & Geography** | Outline maps, compass directions | SVG for outline maps, raster for satellite/detailed |

**SVG tips for history/geography:**
- Timeline diagrams: horizontal line with events marked above/below
- Map outlines: use `<path>` with simplified boundary coordinates
- Use a legend (`<rect>` + `<text>`) for color-coded regions

### 5.4 General Knowledge

| Topic | Diagram Types | Image Source |
|---|---|---|
| **Indian Heritage & Culture** | Monument photos, festival images | Raster |
| **Science & Nature** | Animal photos, natural phenomena | Raster |
| **World Geography** | Country outlines, flag identification | SVG for flags (geometric), raster for maps |

### 5.5 Lower Grades (Classes 1–3) — Future Expansion

When content is extended to lower grades, these diagram types are most appropriate:

| Age Group | Diagram Types |
|---|---|
| **Counting (Class 1–2)** | Groups of objects: apples, stars, dots. SVG circles/rectangles arranged in countable groups |
| **Pattern Recognition (Class 1–3)** | Color/shape sequences (🔴🔵🔴🔵 → ?) using SVG shapes |
| **Letter/Number ID (Class 1–2)** | Large, clear letters/numbers in SVG. "Which letter comes after D?" |
| **Basic Shapes (Class 2–3)** | Simple circle, square, triangle identification |
| **Telling Time (Class 2–3)** | Clock face SVGs with hands at specific times |

**Key principle for lower grades**: Keep SVGs extremely simple. Max 5–6 elements. Large shapes, large text (18–20px). Bold, high-contrast colors.

---

## 6. Quality Checklist

Before committing any image-based question, verify every item:

### SVG Quality

- [ ] **Valid XML**: The SVG string is well-formed XML (all tags closed, attributes quoted)
- [ ] **`xmlns` attribute**: `xmlns="http://www.w3.org/2000/svg"` is present
- [ ] **`viewBox` set**: Uses `0 0 300 200` or `0 0 300 300`
- [ ] **No inline `style` blocks**: Use attributes (`fill`, `stroke`) instead of CSS `<style>` elements for maximum compatibility
- [ ] **No external resources**: No `<image href="...">`, no `@import`, no `<use xlink:href="...">`
- [ ] **Measurements clearly visible**: Font size ≥ 14px, red (#DC2626) color, not overlapping shapes
- [ ] **Sufficient contrast**: Blue shapes on white/light background
- [ ] **No Kannada text in SVG**: All SVG labels use English/numeric values only
- [ ] **Renders correctly**: Test the SVG in a browser before committing

### Question Quality

- [ ] **Answer derivable from image**: The question MUST be answerable by looking at the image. No external knowledge needed beyond what's shown.
- [ ] **Correct answer verified**: Manually compute/verify the answer matches the image data
- [ ] **Distractor quality**: Wrong options are plausible but clearly incorrect upon careful inspection
- [ ] **Single unambiguous answer** (for `image_single`): Only one option can be correct
- [ ] **All correct answers listed** (for `image_multiple`): The `answer` array contains every true statement

### Bilingual Quality

- [ ] **`en` object complete**: `question`, `options`, `answer`, `reasoning` all present
- [ ] **`kn` object complete**: `question`, `options`, `answer`, `reasoning` all present
- [ ] **Answer in options**: `en.answer` ∈ `en.options` and `kn.answer` ∈ `kn.options`
- [ ] **Options count match**: `en.options.length === kn.options.length`
- [ ] **Answer position match**: The correct answer is at the same index in both `en.options` and `kn.options`
- [ ] **`image.alt` bilingual**: Both `en` and `kn` alt text present and accurate

### Raster-Specific Quality

- [ ] **File exists**: The image file exists at `public/images/questions/{src}`
- [ ] **File size ≤ 100 KB**
- [ ] **Dimensions ≤ 600 × 400 px**
- [ ] **Format is WebP or PNG**
- [ ] **No watermarks or copyright text** visible in the image
- [ ] **Image is clear and recognizable** at mobile screen sizes (≥ 320px width)

---

## 7. Content Generation Prompt Template

Copy and customize this prompt when instructing an AI agent to generate image questions:

---

### Template: SVG-Based Image Questions

```
Generate {N} bilingual (English + Kannada) image-based quiz questions for the Bhagiratha Quiz app.

**Target chapter**: {subject} — "{chapter_name}"
**Class**: {class_id} (e.g., class_5, class_6)
**Target file**: src/data/questions/{class_id}/{subject_id}/{chapter_id}.json
**ID prefix**: {prefix}_img_  (e.g., c5_mat_sa_img_)
**Starting index**: {start_index} (e.g., 001)

**Requirements**:
1. Use inline SVG diagrams for all images (no raster).
2. Follow the schema defined in cms/SKILL_image_questions.md §2.1 (image_single) or §2.2 (image_multiple).
3. SVG guidelines:
   - viewBox: 300×200 (landscape) or 300×300 (square)
   - Colors: Blue #2563EB (shapes), Red #DC2626 (measurements), Green #059669 (highlights)
   - Font: Arial, 14px for labels
   - Include xmlns="http://www.w3.org/2000/svg"
   - No Kannada text inside SVG elements
4. Difficulty distribution: {D1_count} easy, {D2_count} medium, {D3_count} hard.
5. Each question's answer MUST be derivable solely from the image.
6. Provide complete Kannada translations for question, options, answer, and reasoning.
7. Alt text must describe the image content accurately in both languages.
8. Verify that en.answer ∈ en.options and kn.answer ∈ kn.options.

**Output format**: A valid JSON array of question objects. No markdown fences, no comments. 
Append these to the existing questions in the target file.
```

### Template: Raster Image Questions

```
Generate {N} bilingual (English + Kannada) image-based quiz questions using photographs.

**Target chapter**: {subject} — "{chapter_name}"
**Class**: {class_id}
**Target file**: src/data/questions/{class_id}/{subject_id}/{chapter_id}.json
**Image directory**: public/images/questions/{class_id}/{subject_id}/
**ID prefix**: {prefix}_img_
**Starting index**: {start_index}

**Requirements**:
1. Use type "image_single" with image.type = "raster".
2. Follow the schema in cms/SKILL_image_questions.md §2.3.
3. Image filenames: {chapter_id}_{NNN}.webp (3-digit zero-padded).
4. Image source: suggest specific Creative Commons images to download, or describe the exact image needed so a human can source it.
5. In the JSON, set image.src to the relative path: "{class_id}/{subject_id}/{chapter_id}_{NNN}.webp".
6. Provide bilingual alt text.
7. Each question's answer MUST be identifiable from the photograph.
8. Verify en.answer ∈ en.options and kn.answer ∈ kn.options.

**Note**: The image files must be sourced, optimized (WebP, ≤100KB, ≤600×400px), and placed in the image directory BEFORE the questions can be used in the app.

**Output format**: A valid JSON array of question objects.
```

### Template: Mixed Batch (SVG + Raster)

```
Generate a mixed batch of {N} image questions for {chapter_name}:
- {SVG_count} SVG-based (geometric diagrams)
- {Raster_count} raster-based (photographs)

Follow all guidelines in cms/SKILL_image_questions.md.
Use IDs: {prefix}_img_{start}  through  {prefix}_img_{end}
Target file: src/data/questions/{class_id}/{subject_id}/{chapter_id}.json
```

---

## 8. Validation

### 8.1 Running the Validator

After creating or modifying image questions, always validate:

```bash
cd /path/to/time-tuk-game
python3 cms/verify_db.py
```

The validator (`cms/verify_db.py`) performs:

1. **JSON parsing**: Ensures all `.json` files in `src/data/questions/` are valid JSON
2. **Schema validation**: Checks that every question has `en` and `kn` objects
3. **Answer-in-options**: Verifies `answer` exists within `options` (for `single` and `image_single`)
4. **Multi-answer validation**: Verifies every element of `answer[]` exists in `options` (for `multiple` and `image_multiple`)
5. **Exact duplicate detection**: Hash-based O(N) check on English question text
6. **Fuzzy duplicate detection**: Catches near-identical questions (>95% similarity)

### 8.2 Image-Specific Validation (To Be Added)

The following checks should be added to `verify_db.py` for image question support:

```python
# Proposed additions to verify_db.py for image questions

def validate_image_questions(questions, issues):
    """Validate image-specific fields."""
    for q in questions:
        q_id = q.get('id', 'unknown')
        file = q.get('_file', 'unknown')
        q_type = q.get('type', 'single')
        
        if q_type not in ('image_single', 'image_multiple'):
            continue
        
        # Check image field exists
        img = q.get('image')
        if not img:
            issues.append(f"[{file}] {q_id} type={q_type} but missing 'image' field")
            continue
        
        # Check image.type
        img_type = img.get('type')
        if img_type not in ('svg', 'raster'):
            issues.append(f"[{file}] {q_id} image.type must be 'svg' or 'raster', got '{img_type}'")
        
        # Check SVG validity
        if img_type == 'svg':
            svg = img.get('svg', '')
            if not svg.strip().startswith('<svg'):
                issues.append(f"[{file}] {q_id} image.svg does not start with '<svg'")
            if 'xmlns' not in svg:
                issues.append(f"[{file}] {q_id} image.svg missing xmlns attribute")
            if not svg.strip().endswith('</svg>'):
                issues.append(f"[{file}] {q_id} image.svg does not end with '</svg>'")
        
        # Check raster file exists
        if img_type == 'raster':
            src = img.get('src', '')
            img_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'public', 'images', 'questions', src
            )
            if not os.path.isfile(img_path):
                issues.append(f"[{file}] {q_id} raster image not found: {src}")
            else:
                size = os.path.getsize(img_path)
                if size > 102400:  # 100 KB
                    issues.append(f"[{file}] {q_id} raster image too large: {size} bytes (max 100KB)")
        
        # Check alt text
        alt = img.get('alt', {})
        if not alt.get('en'):
            issues.append(f"[{file}] {q_id} missing English alt text")
        if not alt.get('kn'):
            issues.append(f"[{file}] {q_id} missing Kannada alt text")
```

### 8.3 Manual SVG Preview

To quickly preview an SVG, create a test HTML file:

```bash
# Quick preview in browser
echo '<html><body style="background:#fff; padding:40px;">' > /tmp/preview.html
echo '<div style="max-width:600px; border:1px solid #ccc; padding:20px;">' >> /tmp/preview.html
# Paste your SVG here
echo '</div></body></html>' >> /tmp/preview.html
open /tmp/preview.html
```

### 8.4 Validation Flowchart

```
Question Created/Edited
         │
         ▼
  python3 cms/verify_db.py
         │
    ┌────┴─────┐
    │ PASS     │ FAIL
    │          │
    ▼          ▼
  Commit    Fix issues listed
             in output, re-run
```

---

## Appendix A: Quick Reference Card

| What | Value |
|---|---|
| SVG viewBox (landscape) | `0 0 300 200` |
| SVG viewBox (square) | `0 0 300 300` |
| Blue (shapes) | `#2563EB` |
| Red (labels) | `#DC2626` |
| Green (highlights) | `#059669` |
| Font | `Arial, sans-serif`, 14px |
| Max raster size | 100 KB |
| Max raster dims | 600 × 400 px |
| Image path | `public/images/questions/{classId}/{subjectId}/{chapterId}_{NNN}.webp` |
| Validator | `python3 cms/verify_db.py` |
| JSON location | `src/data/questions/{classId}/{subjectId}/{chapterId}.json` |

## Appendix B: Catalog Reference

The complete list of valid `classId`, `subjectId`, and `chapterId` values is in:
```
src/data/catalog.json
```

Always cross-reference this file when creating IDs to ensure they map to valid chapters.

### Critical Geometry Requirement: Vertex & Edge Labels
- **ALWAYS label vertices**: Any polygons (triangles, rectangles, squares, etc.) MUST include explicit text labels for their vertices (e.g., A, B, C for triangles; A, B, C, D for rectangles). Place them slightly outside the corners.
- **ALWAYS label edges/angles**: Include text for the lengths of sides (e.g., '5 cm') and measures of angles if they are relevant to the question.
