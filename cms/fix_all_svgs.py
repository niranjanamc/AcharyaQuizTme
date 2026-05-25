import os
import json
import re

directories = [
    '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/',
    '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_6/maths/',
    '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_5/maths/'
]

def fix_svg(svg_str):
    if 'width=' not in svg_str:
        svg_str = svg_str.replace("<svg ", "<svg width='100%' height='100%' ")
    return svg_str

total_fixed = 0
for directory in directories:
    if not os.path.exists(directory): continue
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            changed = False
            for q in data:
                if 'image' in q and q['image'].get('type') == 'svg' and 'svg' in q['image']:
                    old_svg = q['image']['svg']
                    new_svg = fix_svg(old_svg)
                    if old_svg != new_svg:
                        q['image']['svg'] = new_svg
                        changed = True
                if 'en' in q and 'options' in q['en']:
                    for i, opt in enumerate(q['en']['options']):
                        if isinstance(opt, dict) and opt.get('type') == 'svg':
                            old_svg = opt['svg']
                            new_svg = fix_svg(old_svg)
                            if old_svg != new_svg:
                                q['en']['options'][i]['svg'] = new_svg
                                q['kn']['options'][i]['svg'] = new_svg
                                changed = True
                                
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                total_fixed += 1

print(f"Fixed {total_fixed} files.")
