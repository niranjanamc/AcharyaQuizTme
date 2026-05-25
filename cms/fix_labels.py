import json

filepath = 'src/data/questions/class_7/maths/practical_geometry.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

label_a = "<text x='150' y='20' fill='#1F2937' font-family='Arial' font-size='14' text-anchor='middle'>A</text>"
label_b = "<text x='35' y='155' fill='#1F2937' font-family='Arial' font-size='14' text-anchor='middle'>B</text>"
label_c = "<text x='265' y='155' fill='#1F2937' font-family='Arial' font-size='14' text-anchor='middle'>C</text>"

changed = False
for q in data:
    if 'image' in q and q['image'].get('type') == 'svg':
        s = q['image']['svg']
        if "<polygon points='150,30 50,150 250,150'" in s:
            if '>A</text>' not in s:
                s = s.replace("</svg>", f"{label_a}</svg>")
            if '>B</text>' not in s:
                s = s.replace("</svg>", f"{label_b}</svg>")
            if '>C</text>' not in s:
                s = s.replace("</svg>", f"{label_c}</svg>")
            if q['image']['svg'] != s:
                q['image']['svg'] = s
                changed = True

if changed:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Fixed labels in practical_geometry.json")
else:
    print("No changes made.")
