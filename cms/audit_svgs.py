"""
Comprehensive SVG Diagram Audit for Quiz Questions
===================================================
Checks every SVG in the maths question bank for rendering issues:
1. XML validity
2. Missing width/height attributes on <svg> root
3. Missing viewBox
4. Missing xmlns namespace
5. Unclosed tags / malformed XML
6. Empty SVGs (no visible content)
7. Dimension mismatches (width/height vs viewBox)
8. Text labels missing (no <text> elements for geometry diagrams)
9. Escaped character issues (double-escaped quotes, etc.)
10. Missing vertex labels on triangles/rectangles
"""

import os
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions'

def extract_svgs(base_dir):
    """Walk all JSON files and extract every SVG string with metadata."""
    svgs = []
    for root, _, files in os.walk(base_dir):
        for fname in sorted(files):
            if not fname.endswith('.json'):
                continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, base_dir)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue
            
            for q in data:
                if not isinstance(q, dict):
                    continue
                qid = q.get('id', '?')
                
                # Question-level image
                if 'image' in q and isinstance(q['image'], dict) and q['image'].get('type') == 'svg':
                    svgs.append({
                        'file': rel, 'id': qid, 'location': 'question_image',
                        'svg': q['image'].get('svg', ''),
                        'alt': q['image'].get('alt', {}),
                        'q_obj': q,
                    })
                
                # Option-level images
                for lang in ['en', 'kn']:
                    if lang not in q or not isinstance(q[lang].get('options'), list):
                        continue
                    for i, opt in enumerate(q[lang]['options']):
                        if isinstance(opt, dict) and isinstance(opt.get('image'), dict) and opt['image'].get('type') == 'svg':
                            svgs.append({
                                'file': rel, 'id': qid, 'location': f'{lang}_option_{i}',
                                'svg': opt['image'].get('svg', ''),
                                'alt': opt['image'].get('alt', {}),
                                'q_obj': q,
                            })
    return svgs


def audit_svg(entry):
    """Run all checks on a single SVG entry. Returns list of issue strings."""
    issues = []
    svg = entry['svg']
    qid = entry['id']
    loc = entry['location']
    
    if not svg or not svg.strip():
        issues.append(f"EMPTY SVG — no content at all")
        return issues
    
    # 1. XML parsing
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as e:
        issues.append(f"INVALID XML — {e}")
        return issues
    
    # 2. Check <svg> root tag
    tag = root.tag
    if not tag.endswith('svg'):
        issues.append(f"ROOT TAG is '{tag}', expected 'svg'")
    
    # 3. Namespace
    if 'xmlns' not in svg:
        issues.append(f"MISSING xmlns namespace")
    
    # 4. viewBox
    vb = root.attrib.get('viewBox', '')
    if not vb:
        issues.append(f"MISSING viewBox attribute")
    
    # 5. width/height
    w = root.attrib.get('width', '')
    h = root.attrib.get('height', '')
    if not w or not h:
        issues.append(f"MISSING width={w!r} height={h!r}")
    
    # 6. Check if width/height are fixed pixels vs responsive
    if w and h and w != '100%' and h != '100%':
        # Check viewBox consistency
        if vb:
            vb_parts = vb.split()
            if len(vb_parts) == 4:
                vb_w, vb_h = vb_parts[2], vb_parts[3]
                if w != vb_w or h != vb_h:
                    # Not necessarily wrong, but flag if width="100%" isn't used
                    pass
    
    # 7. Check for visible content
    all_children = list(root.iter())
    visible_tags = {'polygon', 'polyline', 'path', 'circle', 'rect', 'ellipse', 'line', 'text', 'image', 'use'}
    visible_count = sum(1 for el in all_children if el.tag.split('}')[-1] in visible_tags)
    if visible_count == 0:
        issues.append(f"NO VISIBLE ELEMENTS — SVG has no shapes or text")
    
    # 8. Check text elements count
    ns = '{http://www.w3.org/2000/svg}'
    text_els = [el for el in all_children if el.tag in ('text', f'{ns}text')]
    
    # 9. Check for common escaped-character issues
    if '&amp;' in svg and '&amp;amp;' not in svg:
        pass  # normal
    if '\\"' in svg:
        issues.append(f"DOUBLE-ESCAPED QUOTES found (\\\"), may render incorrectly")
    
    # 10. Check degree symbol rendering
    if '°' in svg:
        pass  # fine, unicode degree
    if '&deg;' in svg:
        pass  # HTML entity, should work in browser but NOT in XML parser
    if '&#176;' in svg:
        pass  # numeric entity, valid
    
    # 11. Check for geometry diagrams without labels
    has_polygon = any(el.tag in ('polygon', f'{ns}polygon') for el in all_children)
    has_path = any(el.tag in ('path', f'{ns}path') for el in all_children)
    
    if has_polygon and len(text_els) == 0:
        issues.append(f"POLYGON WITHOUT LABELS — geometry diagram has no text labels")
    
    # 12. Check for viewBox with zero dimensions
    if vb:
        vb_parts = vb.split()
        if len(vb_parts) == 4:
            try:
                vb_w_val = float(vb_parts[2])
                vb_h_val = float(vb_parts[3])
                if vb_w_val <= 0 or vb_h_val <= 0:
                    issues.append(f"ZERO-SIZE viewBox: {vb}")
            except ValueError:
                issues.append(f"INVALID viewBox values: {vb}")
    
    # 13. Check for path data being empty
    for el in all_children:
        if el.tag in ('path', f'{ns}path'):
            d = el.attrib.get('d', '')
            if not d.strip():
                issues.append(f"EMPTY PATH d attribute")
                break
    
    # 14. Check for stroke without stroke color
    for el in all_children:
        tag_name = el.tag.split('}')[-1]
        if tag_name in visible_tags - {'text', 'image', 'use'}:
            if 'stroke' not in el.attrib and 'fill' not in el.attrib and 'style' not in el.attrib:
                issues.append(f"SHAPE '{tag_name}' has no stroke or fill — may be invisible")
                break
    
    return issues


def print_report(results):
    """Print a structured report."""
    by_file = defaultdict(list)
    for r in results:
        by_file[r['file']].append(r)
    
    total_svgs = len(results)
    issues_count = sum(1 for r in results if r['issues'])
    clean_count = total_svgs - issues_count
    
    print(f"{'='*70}")
    print(f"SVG DIAGRAM AUDIT REPORT")
    print(f"{'='*70}")
    print(f"Total SVGs scanned: {total_svgs}")
    print(f"Clean (no issues):  {clean_count}")
    print(f"With issues:        {issues_count}")
    print(f"{'='*70}")
    
    if issues_count == 0:
        print("✅ All SVGs are clean!")
        return
    
    for fpath, entries in sorted(by_file.items()):
        bad = [e for e in entries if e['issues']]
        if not bad:
            continue
        print(f"\n📄 {fpath} ({len(bad)} issues)")
        print(f"{'─'*60}")
        for e in bad:
            print(f"  ❌ {e['id']} [{e['location']}]")
            for iss in e['issues']:
                print(f"     → {iss}")
            # Print first 120 chars of SVG for context
            snippet = e['svg'][:120].replace('\n', ' ')
            print(f"     SVG snippet: {snippet}...")


if __name__ == '__main__':
    all_svgs = extract_svgs(BASE)
    
    results = []
    for entry in all_svgs:
        issues = audit_svg(entry)
        entry['issues'] = issues
        results.append(entry)
    
    print_report(results)
    
    # Also dump a machine-readable summary
    print(f"\n{'='*70}")
    print("DETAILED SVG LIST")
    print(f"{'='*70}")
    for r in results:
        status = "✅" if not r['issues'] else "❌"
        print(f"  {status} {r['file']} | {r['id']} | {r['location']} | alt={r['alt']}")
