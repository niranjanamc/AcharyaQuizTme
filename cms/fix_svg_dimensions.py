import os
import json
import re

directory = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/'

def fix_svg(svg_str):
    # If it doesn't have width, add width="300" height="200" (or similar depending on viewBox)
    if 'width=' not in svg_str:
        # Extract viewBox to determine dimensions if possible
        match = re.search(r"viewBox=['\"]0 0 (\d+) (\d+)['\"]", svg_str)
        if match:
            w = match.group(1)
            h = match.group(2)
            svg_str = svg_str.replace('<svg ', f'<svg width="{w}" height="{h}" ')
        else:
            # Fallback
            svg_str = svg_str.replace('<svg ', '<svg width="100%" height="100%" ')
    return svg_str

total_fixed = 0
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
            if 'options' in q.get('en', {}):
                for i, opt in enumerate(q.get('en', {}).get('options', [])):
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
