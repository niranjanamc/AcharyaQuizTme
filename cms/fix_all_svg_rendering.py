"""
Fix ALL SVG rendering issues across the entire question bank.

Issue 1: Missing width/height attributes on <svg> elements.
  - Browser rendering of inline SVGs via dangerouslySetInnerHTML requires
    explicit width/height, otherwise the SVG may collapse to 0x0 or render
    tiny. We add width="100%" height="100%" so it fills the parent container
    responsively, while the viewBox handles aspect ratio.

Issue 2: Polygon without text labels (congruence diagram).
  - We regenerate the specific broken SVG.
"""

import os
import json
import re

BASE = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions'


def fix_svg_dimensions(svg_str):
    """Ensure width='100%' height='100%' on <svg>, replacing existing hardcoded dimensions if present."""
    if not svg_str or '<svg' not in svg_str:
        return svg_str, False
    
    changed = False
    
    # Strip existing width="xxx" and height="xxx" attributes that are not 100%
    if re.search(r'<svg[^>]+\bwidth=["\'](?!100%)[^"\']+["\']', svg_str) or re.search(r'<svg[^>]+\bheight=["\'](?!100%)[^"\']+["\']', svg_str):
        svg_str = re.sub(r'(<svg[^>]+)\bwidth=["\'][^"\']+["\']', r'\1', svg_str)
        svg_str = re.sub(r'(<svg[^>]+)\bheight=["\'][^"\']+["\']', r'\1', svg_str)
        # Clean up any multiple spaces created by stripping
        svg_str = re.sub(r'(<svg[^>]+)\s+>', r'\1>', svg_str)
        changed = True

    # If width="100%" is missing, add it
    if 'width="100%"' not in svg_str and "width='100%'" not in svg_str:
        svg_str = re.sub(r'<svg\b', '<svg width="100%" height="100%"', svg_str, count=1)
        changed = True
        
    return svg_str, changed


def fix_congruence_012():
    """Regenerate the specific congruence diagram that is missing labels."""
    return (
        '<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">'
        '<polygon points="30,170 100,40 170,170" fill="none" stroke="#2563EB" stroke-width="2"/>'
        '<polygon points="130,170 200,40 270,170" fill="none" stroke="#2563EB" stroke-width="2"/>'
        # Vertex labels - Triangle 1
        '<text x="22" y="180" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold">A</text>'
        '<text x="95" y="30" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold">B</text>'
        '<text x="175" y="180" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold">C</text>'
        # Vertex labels - Triangle 2
        '<text x="122" y="180" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold">P</text>'
        '<text x="195" y="30" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold">Q</text>'
        '<text x="275" y="180" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold">R</text>'
        # Side equality marks (tick marks on AB=PQ)
        '<line x1="62" y1="100" x2="68" y2="108" stroke="#DC2626" stroke-width="2"/>'
        '<line x1="162" y1="100" x2="168" y2="108" stroke="#DC2626" stroke-width="2"/>'
        # Side equality marks (tick marks on BC=QR, double)
        '<line x1="133" y1="100" x2="139" y2="108" stroke="#DC2626" stroke-width="2"/>'
        '<line x1="136" y1="100" x2="142" y2="108" stroke="#DC2626" stroke-width="2"/>'
        '<line x1="233" y1="100" x2="239" y2="108" stroke="#DC2626" stroke-width="2"/>'
        '<line x1="236" y1="100" x2="242" y2="108" stroke="#DC2626" stroke-width="2"/>'
        # Angle arcs at B and Q (included angle)
        '<path d="M88,55 A15,15 0 0,1 112,55" fill="none" stroke="#059669" stroke-width="1.5"/>'
        '<path d="M188,55 A15,15 0 0,1 212,55" fill="none" stroke="#059669" stroke-width="1.5"/>'
        '</svg>'
    )


def process_all_files():
    total_fixed = 0
    files_changed = 0
    
    for root, _, files in os.walk(BASE):
        for fname in sorted(files):
            if not fname.endswith('.json'):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue
            
            file_changed = False
            
            for q in data:
                if not isinstance(q, dict):
                    continue
                qid = q.get('id', '')
                
                # Special case: congruence unlabeled polygon
                if qid == 'c7_math_cong_img_012' and 'image' in q:
                    q['image']['svg'] = fix_congruence_012()
                    file_changed = True
                    total_fixed += 1
                    continue
                
                # Fix question-level image
                if 'image' in q and isinstance(q['image'], dict) and q['image'].get('type') == 'svg':
                    svg = q['image'].get('svg', '')
                    new_svg, changed = fix_svg_dimensions(svg)
                    if changed:
                        q['image']['svg'] = new_svg
                        file_changed = True
                        total_fixed += 1
                
                # Fix option-level images
                for lang in ['en', 'kn']:
                    if lang not in q or not isinstance(q[lang].get('options'), list):
                        continue
                    for i, opt in enumerate(q[lang]['options']):
                        if isinstance(opt, dict) and isinstance(opt.get('image'), dict) and opt['image'].get('type') == 'svg':
                            svg = opt['image'].get('svg', '')
                            new_svg, changed = fix_svg_dimensions(svg)
                            if changed:
                                q[lang]['options'][i]['image']['svg'] = new_svg
                                file_changed = True
                                total_fixed += 1
            
            if file_changed:
                with open(fpath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                files_changed += 1
    
    return total_fixed, files_changed


if __name__ == '__main__':
    total_fixed, files_changed = process_all_files()
    print(f"Fixed {total_fixed} SVGs across {files_changed} files.")
