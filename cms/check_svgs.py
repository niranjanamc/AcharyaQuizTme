import os
import json
import xml.etree.ElementTree as ET

def check_svgs(dir_path):
    issues = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if not file.endswith('.json'): continue
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except Exception as e:
                    continue
            
            for q in data:
                # Check option images
                for lang in ['en', 'kn']:
                    if lang in q and isinstance(q[lang].get('options'), list):
                        for i, opt in enumerate(q[lang]['options']):
                            if isinstance(opt, dict) and 'image' in opt and isinstance(opt['image'], dict) and opt['image'].get('type') == 'svg':
                                svg = opt['image'].get('svg', '')
                                try:
                                    ET.fromstring(svg)
                                except Exception as e:
                                    issues.append(f"{path} | {q.get('id')} {lang} opt {i} SVG error: {e}")
                
                # Check question images
                if 'image' in q and isinstance(q['image'], dict) and q['image'].get('type') == 'svg':
                    svg = q['image'].get('svg', '')
                    try:
                        ET.fromstring(svg)
                    except Exception as e:
                        issues.append(f"{path} | {q.get('id')} main SVG error: {e}")
    return issues

if __name__ == '__main__':
    all_issues = check_svgs('src/data/questions/class_7/maths')
    all_issues += check_svgs('src/data/questions/class_6/maths')
    all_issues += check_svgs('src/data/questions/class_5/maths')
    if all_issues:
        print("Found SVG Issues:")
        for iss in all_issues:
            print(iss)
    else:
        print("All SVGs are valid XML.")
