import json
import glob

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return
        
    if not isinstance(data, list):
        return
        
    changed = False
    for q in data:
        if not isinstance(q, dict):
            continue
        if q.get('image') and isinstance(q['image'], dict) and q['image'].get('type') == 'svg':
            svg = q['image']['svg']
            if '\\"' in svg:
                q['image']['svg'] = svg.replace('\\"', '"')
                changed = True
        
        # Also check options for images
        for lang in ['en', 'kn']:
            if lang in q and 'options' in q[lang]:
                for opt in q[lang]['options']:
                    if isinstance(opt, dict) and 'image' in opt and opt['image'].get('type') == 'svg':
                        svg = opt['image']['svg']
                        if '\\"' in svg:
                            opt['image']['svg'] = svg.replace('\\"', '"')
                            changed = True
                            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed {filepath}")

for f in glob.glob('src/data/questions/**/*.json', recursive=True):
    fix_file(f)
