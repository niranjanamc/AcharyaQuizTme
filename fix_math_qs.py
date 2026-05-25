import json
import os

OUT_DIR = "/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths"
FILES = [
    ("rational_numbers.json", "c7_math_rat_"),
    ("practical_geometry.json", "c7_math_geom_"),
    ("perimeter_area.json", "c7_math_perim_"),
    ("algebraic_expressions.json", "c7_math_alg_")
]

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(p, data):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def replace_in_q(q):
    s = json.dumps(q)
    # rational numbers
    s = s.replace("equivalent to 1/2", "equivalent to 1/3")
    s = s.replace("15/20", "18/24")
    s = s.replace("1/5 and 2/5", "1/7 and 2/7")
    s = s.replace("6/18 in its simplest form", "simplest form of 12/36")
    s = s.replace("Match the operation with its result.", "Match the rational number operation to its result.")
    # geometry
    s = s.replace("Match the triangle type to its property.", "Match each geometric figure property with its specific name.")
    # algebra
    s = s.replace("Which of the following is a trinomial?", "Identify the algebraic expression that represents a trinomial.")
    s = s.replace("Which of the following is a binomial?", "Identify the algebraic expression that represents a binomial.")
    return json.loads(s)

for filename, prefix in FILES:
    filepath = os.path.join(OUT_DIR, filename)
    if not os.path.exists(filepath):
        continue
    data = load_json(filepath)
    
    # Process replacements
    new_data = [replace_in_q(q) for q in data]
    
    # Bucket by difficulty
    easy = [q for q in new_data if q['difficulty'] == 1]
    med = [q for q in new_data if q['difficulty'] == 2]
    hard = [q for q in new_data if q['difficulty'] == 3]
    
    # Take exactly 10 of each
    final_qs = easy[:10] + med[:10] + hard[:10]
    
    # Re-index
    for i, q in enumerate(final_qs, start=1):
        q['id'] = f"{prefix}{i:03d}"
        
    save_json(filepath, final_qs)
    print(f"Fixed {filename}, count={len(final_qs)}")
