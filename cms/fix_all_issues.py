import json
import os

BASE = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions'

def load_json(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(fpath, data):
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fix_all():
    # 1. Natural Phenomena
    fpath = os.path.join(BASE, 'class_8/science/natural_phenomena.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_sci_nat_024':
            q['kn']['answer'] = [
                'ಟೆಕ್ಟಾನಿಕ್ ತಟ್ಟೆಗಳು ವರ್ಷಕ್ಕೆ ಕೆಲವು ಸೆಂಟಿಮೀಟರ್‌ಗಳಷ್ಟು ಅತ್ಯಂತ ನಿಧಾನಗತಿಯಲ್ಲಿ ಚಲಿಸುತ್ತಿರುತ್ತವೆ',
                'ಘರ್ಷಣೆಯ ಕಾರಣದಿಂದಾಗಿ ತಟ್ಟೆಗಳ ಗಡಿಯಲ್ಲಿ ಒತ್ತಡ ಸಂಗ್ರಹವಾಗುತ್ತದೆ, ಇದು ಭೂಕಂಪನವಾಗಿ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ'
            ]
    save_json(fpath, data)
    print("Fixed natural_phenomena.json")

    # 2. Coal & Petroleum
    fpath = os.path.join(BASE, 'class_8/science/coal_petroleum.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_sci_coal_024':
            q['kn']['answer'] = "ಪೆಟ್ರೋಕೆಮಿಕಲ್ಸ್ (Petrochemicals)"
    save_json(fpath, data)
    print("Fixed coal_petroleum.json")

    # 3. Bepin's Memory
    fpath = os.path.join(BASE, 'class_8/english/c8_eng_bepin.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_eng_bepin_010':
            q['kn']['answer'] = "ಹರಿದಾಸ್ ತಮ್ಮ ಪತ್ನಿಯೊಂದಿಗೆ ಜಪಾನ್‌ಗೆ ಹೋಗಿದ್ದರು ಮತ್ತು ಬೆಪಿನ್ ಅವರ ಬಳಿ ಹೊಸ ವಿಳಾಸ ಇರಲಿಲ್ಲ"
    save_json(fpath, data)
    print("Fixed c8_eng_bepin.json")

    # 4. Glimpses of the Past
    fpath = os.path.join(BASE, 'class_8/english/c8_eng_glimpses.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_eng_glim_001':
            q['kn']['answer'] = "ಲತಾ ಮಂಗೇಶ್ಕರ್"
    save_json(fpath, data)
    print("Fixed c8_eng_glimpses.json")

    # 5. Data Handling
    fpath = os.path.join(BASE, 'class_8/maths/data_handling.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_data_img_016':
            q['kn']['answer'] = "10 ಅಂಕಗಳು"
        if q['id'] == 'c8_math_data_001':
            # Rephrase duplicate from Class 6
            q['en']['question'] = "What name is given to a representation of data that uses pictures or symbols?"
            q['kn']['question'] = "ಚಿತ್ರಗಳು ಅಥವಾ ಚಿಹ್ನೆಗಳನ್ನು ಬಳಸುವ ದತ್ತಾಂಶದ ಪ್ರತಿನಿಧಿಸುವಿಕೆಗೆ ಯಾವ ಹೆಸರನ್ನು ನೀಡಲಾಗಿದೆ?"
        if q['id'] == 'c8_math_data_004':
            # Revert to original meaning
            q['en']['question'] = "When data is grouped into ranges like 0-10 or 10-20, what is each group called?"
            q['kn']['question'] = "ದತ್ತಾಂಶವನ್ನು 0-10 ಅಥವಾ 10-20 ರಂತಹ ವ್ಯಾಪ್ತಿಗಳಲ್ಲಿ ವರ್ಗೀಕರಿಸಿದಾಗ, ಪ್ರತಿ ಗುಂಪನ್ನು ಏನೆಂದು ಕರೆಯಲಾಗುತ್ತದೆ?"
    save_json(fpath, data)
    print("Fixed data_handling.json")

    # 6. Quadrilaterals
    fpath = os.path.join(BASE, 'class_8/maths/quadrilaterals.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_quad_018':
            q['image'] = {
                "type": "svg",
                "svg": '<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200"><polygon points="150,20 240,80 150,180 60,80" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/><line x1="150" y1="20" x2="150" y2="180" stroke="#EA580C" stroke-width="1.5" stroke-dasharray="5,5"/><line x1="60" y1="80" x2="240" y2="80" stroke="#EA580C" stroke-width="1.5" stroke-dasharray="5,5"/><text x="150" y="15" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" font-weight="bold">A</text><text x="248" y="80" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="start" font-weight="bold">B</text><text x="150" y="195" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" font-weight="bold">C</text><text x="52" y="80" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="end" font-weight="bold">D</text><text x="156" y="94" fill="#DC2626" font-family="Arial, sans-serif" font-size="10" font-weight="bold">90°</text><path d="M150,70 L160,70 L160,80" fill="none" stroke="#EA580C" stroke-width="1"/></svg>',
                "alt": {
                  "en": "A diagram of a kite ABCD with diagonals AC and BD intersecting at 90 degrees.",
                  "kn": "ಕರ್ಣಗಳು AC ಮತ್ತು BD ಯು 90 ಡಿಗ್ರಿ ಕೋನದಲ್ಲಿ ಛೇದಿಸುವ ABCD ಗಾಳಿಪಟದ ರೇಖಾಚಿತ್ರ."
                }
            }
    save_json(fpath, data)
    print("Fixed quadrilaterals.json")

    # 7 & 8. Linear Equations
    fpath = os.path.join(BASE, 'class_8/maths/linear_equations.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_lin_014':
            q['kn']['answer'] = "45 ಮತ್ತು 27"
        if q['id'] == 'c8_math_lin_022':
            q['kn']['answer'] = "14 ವರ್ಷಗಳು"
    save_json(fpath, data)
    print("Fixed linear_equations.json")

    # 9. History Trade (Duplicate)
    fpath = os.path.join(BASE, 'class_8/history/c8_his_trade.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_his_trade_022':
            q['en']['question'] = "Match the British historical terms of trade with their correct explanations:"
            q['kn']['question'] = "ಬ್ರಿಟಿಷ್ ಇತಿಹಾಸದ ವ್ಯಾಪಾರ ನಿಯಮಗಳನ್ನು ಅವುಗಳ ಸರಿಯಾದ ವಿವರಣೆಗಳೊಂದಿಗೆ ಹೊಂದಿಸಿ:"
        if q['id'] == 'c8_his_trade_023':
            q['en']['question'] = "Match the historical battles and annexations with their correct years:"
            q['kn']['question'] = "ಐತಿಹಾಸಿಕ ಯುದ್ಧಗಳು ಮತ್ತು ಸ್ವಾಧೀನಗಳನ್ನು ಅವುಗಳ ಸರಿಯಾದ ವರ್ಷಗಳೊಂದಿಗೆ ಹೊಂದಿಸಿ:"
    save_json(fpath, data)
    print("Fixed c8_his_trade.json")

    # 10. Cubes and Cube Roots (Fuzzy duplicates)
    fpath = os.path.join(BASE, 'class_8/maths/cubes_roots.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_cub_009':
            q['en']['question'] = "Compute the cube root of the integer 8000:"
            q['kn']['question'] = "ಪೂರ್ಣಾಂಕ 8000 ರ ಘನಮೂಲವನ್ನು ಲೆಕ್ಕಾಚಾರ ಮಾಡಿ:"
        if q['id'] == 'c8_math_cub_008':
            q['en']['question'] = "Identify which numbers among the options are not perfect cubes:"
            q['kn']['question'] = "ಆಯ್ಕೆಗಳಲ್ಲಿ ಯಾವ ಸಂಖ್ಯೆಗಳು ಪರಿಪೂರ್ಣ ಘನಗಳಲ್ಲ ಎಂಬುದನ್ನು ಗುರುತಿಸಿ:"
        if q['id'] == 'c8_math_cub_005':
            q['en']['question'] = "Match the numbers shown on the left with their corresponding perfect cube values:"
            q['kn']['question'] = "ಎಡಭಾಗದಲ್ಲಿ ತೋರಿಸಿರುವ ಸಂಖ್ಯೆಗಳನ್ನು ಅವುಗಳ ಅನುರೂಪ ಪರಿಪೂರ್ಣ ಘನ ಮೌಲ್ಯಗಳೊಂದಿಗೆ ಹೊಂದಿಸಿ:"
        if q['id'] == 'c8_math_cub_024':
            q['en']['question'] = "Which of the statements below regarding perfect cubes are true?"
            q['kn']['question'] = "ಪರಿಪೂರ್ಣ ಘನಗಳ ಕುರಿತು ಕೆಳಗಿನ ಯಾವ ಹೇಳಿಕೆಗಳು ನಿಜವಾಗಿವೆ?"
    save_json(fpath, data)
    print("Fixed cubes_roots.json")

    # 11. Algebraic Expressions (Fuzzy duplicates)
    fpath = os.path.join(BASE, 'class_8/maths/algebraic_expressions.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_alg_015':
            q['en']['question'] = "Calculate the numerical value of (98)² using an appropriate identity."
            q['kn']['question'] = "ಸೂಕ್ತವಾದ ನಿತ್ಯಸಮೀಕರಣವನ್ನು ಬಳಸಿಕೊಂಡು (98)² ರ ಸಂಖ್ಯಾತ್ಮಕ ಮೌಲ್ಯವನ್ನು ಲೆಕ್ಕಾಚಾರ ಮಾಡಿ."
    save_json(fpath, data)
    print("Fixed algebraic_expressions.json")

    # 12. Graphs (Fuzzy duplicates)
    fpath = os.path.join(BASE, 'class_8/maths/graphs.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_graph_002':
            q['en']['question'] = "Determine the exact location of the point (3, 0) on the coordinate axes."
            q['kn']['question'] = "ನಿರ್ದೇಶಾಂಕ ಅಕ್ಷಗಳ ಮೇಲೆ (3, 0) ಬಿಂದುವಿನ ನಿಖರವಾದ ಸ್ಥಾನವನ್ನು ನಿರ್ಧರಿಸಿ."
        if q['id'] == 'c8_math_graph_004':
            q['en']['question'] = "For the coordinate pair (5, 8), what is the alternative term for the y-coordinate?"
            q['kn']['question'] = "ನಿರ್ದೇಶಾಂಕ ಜೋಡಿ (5, 8) ಗಾಗಿ, y-ನಿರ್ದೇಶಾಂಕದ ಪರ್ಯಾಯ ಪದ ಯಾವುದು?"
    save_json(fpath, data)
    print("Fixed graphs.json")

    # 13. Factorisation (Fuzzy duplicate)
    fpath = os.path.join(BASE, 'class_8/maths/factorisation.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_fact_017':
            q['en']['question'] = "Which of the following algebraic expressions have (x - 5) as one of their factors? (Select all that apply)"
            q['kn']['question'] = "ಕೆಳಗಿನ ಬೀಜೋಕ್ತಿಗಳಲ್ಲಿ ಯಾವುದು (x - 5) ಅನ್ನು ಒಂದು ಅಪವರ್ತನವಾಗಿ ಹೊಂದಿದೆ? (ಅನ್ವಯಿಸುವ ಎಲ್ಲವನ್ನೂ ಆರಿಸಿ)"
        if q['id'] == 'c8_math_fact_027':
            q['en']['question'] = "Find which of the algebraic expressions listed are equivalent to (2x - 3y)²."
            q['kn']['question'] = "ಪಟ್ಟಿಯಲ್ಲಿರುವ ಯಾವ ಬೀಜೋಕ್ತಿಗಳು (2x - 3y)² ಗೆ ಸಮನಾಗಿವೆ ಎಂಬುದನ್ನು ಕಂಡುಕೊಳ್ಳಿ."
    save_json(fpath, data)
    print("Fixed factorisation.json")

    # 14. Adolescence (Fuzzy duplicate)
    fpath = os.path.join(BASE, 'class_8/science/adolescence.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_sci_adol_009':
            q['en']['question'] = "Choose all the secondary sexual characteristics that develop in boys when they undergo puberty:"
            q['kn']['question'] = "HUಡುಗರು ಹದಿಹರೆಯಕ್ಕೆ ಒಳಗಾದಾಗ ಅವರಲ್ಲಿ ಬೆಳೆಯುವ ಎಲ್ಲಾ ದ್ವಿತೀಯ ಲೈಂಗಿಕ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಆರಿಸಿ:"
    save_json(fpath, data)
    print("Fixed adolescence.json")

    # 15. Proportions (Fuzzy duplicate)
    fpath = os.path.join(BASE, 'class_8/maths/proportions.json')
    data = load_json(fpath)
    for q in data:
        if q['id'] == 'c8_math_prop_004':
            q['en']['question'] = "From the options below, select all the situations that represent an inverse proportion:"
            q['kn']['question'] = "ಕೆಳಗಿನ ಆಯ್ಕೆಗಳಿಂದ, ವಿಲೋಮ ಅನುಪಾತವನ್ನು ಪ್ರತಿನಿಧಿಸುವ ಎಲ್ಲಾ ಸಂದರ್ಭಗಳನ್ನು ಆರಿಸಿ:"
    save_json(fpath, data)
    print("Fixed proportions.json")

if __name__ == '__main__':
    fix_all()
