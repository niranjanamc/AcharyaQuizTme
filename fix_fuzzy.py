import json

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(p, data):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def replace_in_q(q):
    s = json.dumps(q)
    s = s.replace("What is the sum of 1/7 and 2/7?", "Add the rational numbers 1/7 and 2/7.")
    s = s.replace("Which of the following fractions are equivalent to 1/3?", "Identify the fractions that have the same value as 1/3.")
    s = s.replace("Identify the algebraic expression that represents a binomial.", "Which mathematical expression contains exactly two terms?")
    return json.loads(s)

files = [
    "src/data/questions/class_7/maths/rational_numbers.json",
    "src/data/questions/class_7/maths/algebraic_expressions.json"
]

for filepath in files:
    data = load_json(filepath)
    new_data = [replace_in_q(q) for q in data]
    save_json(filepath, new_data)
