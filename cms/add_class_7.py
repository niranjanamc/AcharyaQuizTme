import json
import os

catalog_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/catalog.json'

with open(catalog_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find if class_7 exists
class_7 = next((c for c in data['classes'] if c['id'] == 'class_7'), None)

if not class_7:
    class_7 = {
        "id": "class_7",
        "name": "Class 7 (NCERT)",
        "subjects": []
    }
    data['classes'].append(class_7)

# Check if maths subject exists
maths_subject = next((s for s in class_7['subjects'] if s['id'] == 'maths'), None)

if not maths_subject:
    maths_subject = {
        "id": "maths",
        "name": "Mathematics (Math-Magic)",
        "chapters": [
            { "id": "integers", "name": "Integers" },
            { "id": "fractions_decimals", "name": "Fractions and Decimals" },
            { "id": "data_handling", "name": "Data Handling" },
            { "id": "simple_equations", "name": "Simple Equations" },
            { "id": "lines_angles", "name": "Lines and Angles" },
            { "id": "triangles", "name": "The Triangle and its Properties" },
            { "id": "congruence", "name": "Congruence of Triangles" },
            { "id": "comparing_quantities", "name": "Comparing Quantities" },
            { "id": "rational_numbers", "name": "Rational Numbers" },
            { "id": "practical_geometry", "name": "Practical Geometry" },
            { "id": "perimeter_area", "name": "Perimeter and Area" },
            { "id": "algebraic_expressions", "name": "Algebraic Expressions" },
            { "id": "exponents_powers", "name": "Exponents and Powers" },
            { "id": "symmetry", "name": "Symmetry" },
            { "id": "solid_shapes", "name": "Visualising Solid Shapes" }
        ]
    }
    class_7['subjects'].append(maths_subject)

with open(catalog_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added class 7 to catalog.json")
