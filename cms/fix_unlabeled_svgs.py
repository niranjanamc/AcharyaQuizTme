"""
Add labels to the 3 remaining maths SVGs that have polygons without text labels.
The 2 science SVGs are visual diagrams that don't need vertex labels.
"""
import json

def fix_solid_018():
    """Pyramid diagram — add vertex labels and face labels."""
    return (
        '<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">'
        # Front triangle face
        '<polygon points="150,50 80,200 220,200" fill="none" stroke="#2563EB" stroke-width="2"/>'
        # Vertical height line
        '<line x1="150" y1="50" x2="150" y2="200" stroke="#2563EB" stroke-width="1" stroke-dasharray="4,4"/>'
        # Base triangle
        '<polygon points="80,200 220,200 150,240" fill="none" stroke="#2563EB" stroke-width="2"/>'
        # Hidden edge
        '<line x1="150" y1="50" x2="150" y2="240" stroke="#2563EB" stroke-width="1" stroke-dasharray="4,4"/>'
        # Vertex labels
        '<text x="150" y="40" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">A (Apex)</text>'
        '<text x="65" y="210" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">B</text>'
        '<text x="235" y="210" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">C</text>'
        '<text x="150" y="255" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">D</text>'
        # Height label
        '<text x="135" y="135" fill="#DC2626" font-family="Arial" font-size="12" text-anchor="end">h</text>'
        '</svg>'
    )

def fix_symm_018():
    """Isosceles triangle with one line of symmetry — add vertex labels and symmetry line label."""
    return (
        '<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">'
        # Triangle
        '<polygon points="150,30 50,170 250,170" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>'
        # Symmetry line (dashed red)
        '<line x1="150" y1="10" x2="150" y2="190" stroke="#DC2626" stroke-width="2" stroke-dasharray="5,5"/>'
        # Vertex labels
        '<text x="150" y="22" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">A</text>'
        '<text x="38" y="180" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">B</text>'
        '<text x="262" y="180" fill="#1F2937" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">C</text>'
        # Equal side marks (tick marks on AB and AC)
        '<line x1="98" y1="94" x2="105" y2="102" stroke="#059669" stroke-width="2"/>'
        '<line x1="195" y1="102" x2="202" y2="94" stroke="#059669" stroke-width="2"/>'
        '</svg>'
    )

def fix_symm_019():
    """Regular hexagon — add vertex labels."""
    return (
        '<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">'
        # Hexagon
        '<polygon points="150,30 250,80 250,180 150,230 50,180 50,80" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>'
        # 6 lines of symmetry (dashed)
        '<line x1="150" y1="15" x2="150" y2="245" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="5,5"/>'
        '<line x1="50" y1="80" x2="250" y2="180" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="5,5"/>'
        '<line x1="50" y1="180" x2="250" y2="80" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="5,5"/>'
        '<line x1="35" y1="130" x2="265" y2="130" stroke="#DC2626" stroke-width="1" stroke-dasharray="3,3"/>'
        '<line x1="100" y1="50" x2="200" y2="210" stroke="#DC2626" stroke-width="1" stroke-dasharray="3,3"/>'
        '<line x1="200" y1="50" x2="100" y2="210" stroke="#DC2626" stroke-width="1" stroke-dasharray="3,3"/>'
        # Vertex labels
        '<text x="150" y="20" fill="#1F2937" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle">A</text>'
        '<text x="262" y="78" fill="#1F2937" font-family="Arial" font-size="13" font-weight="bold" text-anchor="start">B</text>'
        '<text x="262" y="188" fill="#1F2937" font-family="Arial" font-size="13" font-weight="bold" text-anchor="start">C</text>'
        '<text x="150" y="250" fill="#1F2937" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle">D</text>'
        '<text x="36" y="188" fill="#1F2937" font-family="Arial" font-size="13" font-weight="bold" text-anchor="end">E</text>'
        '<text x="36" y="78" fill="#1F2937" font-family="Arial" font-size="13" font-weight="bold" text-anchor="end">F</text>'
        # Count label
        '<text x="150" y="140" fill="#DC2626" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">6 lines</text>'
        '</svg>'
    )


fixes = {
    'c7_math_solid_018': fix_solid_018,
    'c7_math_symm_018': fix_symm_018,
    'c7_math_symm_019': fix_symm_019,
}

files_to_check = [
    'src/data/questions/class_7/maths/solid_shapes.json',
    'src/data/questions/class_7/maths/symmetry.json',
]

for fpath in files_to_check:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changed = False
    for q in data:
        qid = q.get('id', '')
        if qid in fixes:
            q['image']['svg'] = fixes[qid]()
            changed = True
            print(f"  Fixed {qid}")
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

print("Done fixing remaining unlabeled polygons")
