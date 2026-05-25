import json

filepath = 'src/data/questions/class_7/maths/practical_geometry.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

changed = 0
for q in data:
    if 'image' in q and q['image'].get('type') == 'svg':
        s = q['image']['svg']
        if 'width=' not in s:
            s = s.replace('<svg ', '<svg width="100%" height="100%" ')
            q['image']['svg'] = s
            changed += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Fixed {changed} SVGs in practical_geometry")
