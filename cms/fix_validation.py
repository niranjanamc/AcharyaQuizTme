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
            if 'kn_ans' in fix:
                q['kn']['answer'] = fix['kn_ans']
                changed = True
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

fixes_symmetry = {
    'c7_math_symm_003': {'kn_ans': 'ಅನಂತ'},
    'c7_math_symm_008': {'kn_ans': 'ಅನಂತ'},
    'c7_math_symm_019': {'en_q': 'Determine the number of lines of symmetry for a regular hexagon.'},
    'c7_math_symm_004': {'en_q': 'Determine the number of lines of symmetry in the uppercase letter A.'},
    'c7_math_symm_005': {'en_q': 'Determine the number of lines of symmetry in the uppercase letter Z.'},
    'c7_math_symm_017': {'en_q': 'Find the order of rotational symmetry for this given shape.'}
}
fix_file('src/data/questions/class_7/maths/symmetry.json', fixes_symmetry)

fixes_solid = {
    'c7_math_solid_020': {'en_q': 'Identify the 3D shape that this net forms when folded.'}
}
fix_file('src/data/questions/class_7/maths/solid_shapes.json', fixes_solid)

fixes_exp = {
    'c7_math_exp_006': {'en_q': 'Evaluate the expression (-1)^5.'}
}
fix_file('src/data/questions/class_7/maths/exponents_powers.json', fixes_exp)

fixes_frac = {
    'c7_math_frac_019': {'en_q': 'Identify the set of proper fractions from the following options.'}
}
fix_file('src/data/questions/class_7/maths/fractions_decimals.json', fixes_frac)

