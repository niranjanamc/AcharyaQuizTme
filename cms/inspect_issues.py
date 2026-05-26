import json
import os

BASE = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions'

def inspect(file_rel, qid):
    path = os.path.join(BASE, file_rel)
    if not os.path.exists(path):
        print(f"File {file_rel} not found")
        return
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    q = next((item for item in data if item.get('id') == qid), None)
    if q:
        print(f"\n--- {file_rel} : {qid} ---")
        print(json.dumps(q, indent=2, ensure_ascii=False))
    else:
        print(f"Question {qid} not found in {file_rel}")

# Inspect the problematic questions
inspect('class_8/science/natural_phenomena.json', 'c8_sci_nat_024')
inspect('class_8/science/coal_petroleum.json', 'c8_sci_coal_024')
inspect('class_8/english/c8_eng_bepin.json', 'c8_eng_bepin_010')
inspect('class_8/english/c8_eng_glimpses.json', 'c8_eng_glim_001')
inspect('class_8/maths/data_handling.json', 'c8_math_data_img_016')
inspect('class_8/maths/quadrilaterals.json', 'c8_math_quad_018')
inspect('class_8/maths/linear_equations.json', 'c8_math_lin_014')
inspect('class_8/maths/linear_equations.json', 'c8_math_lin_022')
