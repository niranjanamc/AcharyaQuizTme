import json

files = ["rational_numbers.json", "practical_geometry.json", "perimeter_area.json", "algebraic_expressions.json"]
for f in files:
    with open(f"src/data/questions/class_7/maths/{f}") as file:
        data = json.load(file)
        e = sum(1 for q in data if q['difficulty'] == 1)
        m = sum(1 for q in data if q['difficulty'] == 2)
        h = sum(1 for q in data if q['difficulty'] == 3)
        print(f"{f}: E={e} M={m} H={h} Total={len(data)}")
