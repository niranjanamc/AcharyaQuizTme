import json

def fix_file(filepath, fixes):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    changed = False
    for q in data:
        if q['id'] in fixes:
            fix = fixes[q['id']]
            if 'en_q' in fix:
                q['en']['question'] = fix['en_q']
                changed = True
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

fixes_symmetry = {
    'c7_math_symm_005': {'en_q': 'How many symmetry lines exist for the capital letter Z?'}
}
fix_file('src/data/questions/class_7/maths/symmetry.json', fixes_symmetry)

