import os
import json
from difflib import SequenceMatcher
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'data', 'questions')
SIMILARITY_THRESHOLD = 0.95

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def verify_db():
    all_questions = []
    issues = []

    # 1. Load all valid question JSON files
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for q in data:
                                q['_file'] = os.path.relpath(path, DATA_DIR)
                                all_questions.append(q)
                except Exception as e:
                    issues.append(f"Error reading {file}: {e}")

    print(f"Loaded {len(all_questions)} questions across database.")

    # 2. Schema Validation & gathering valid questions
    valid_questions = []
    
    # Resolve the project root for raster image file existence checks
    project_root = os.path.dirname(os.path.dirname(__file__))
    images_dir = os.path.join(project_root, 'public', 'images', 'questions')

    for idx, q in enumerate(all_questions):
        q_id = q.get('id', f"UnknownID_{idx}")
        file = q.get('_file')
        
        # Schema Checks
        if 'en' not in q or 'kn' not in q:
            issues.append(f"[{file}] Question {q_id} missing 'en' or 'kn' objects.")
            continue
            
        en = q['en']
        kn = q['kn']
        
        q_type = q.get('type', 'single')

        # Map image types to their effective answer type
        effective_type = q_type
        if q_type == 'image_single':
            effective_type = 'single'
        elif q_type == 'image_multiple':
            effective_type = 'multiple'

        # Validate the image field for image-based question types
        if q_type in ('image_single', 'image_multiple'):
            img = q.get('image')
            
            # Check if options have images
            opts_have_images = any(isinstance(opt, dict) and 'image' in opt for lang_opts in (q.get('en', {}).get('options', []), q.get('kn', {}).get('options', [])) for opt in lang_opts)
            
            if not img and not opts_have_images:
                issues.append(f"[{file}] {q_id} image-type question missing 'image' field and no options have images.")
            elif img and not isinstance(img, dict):
                issues.append(f"[{file}] {q_id} 'image' field must be an object.")
            elif img:
                img_type = img.get('type')
                if img_type not in ('svg', 'raster'):
                    issues.append(f"[{file}] {q_id} image.type must be 'svg' or 'raster', got '{img_type}'.")
                elif img_type == 'svg':
                    svg_str = img.get('svg', '')
                    if not isinstance(svg_str, str) or len(svg_str.strip()) == 0:
                        issues.append(f"[{file}] {q_id} image.svg must be a non-empty string.")
                    else:
                        if 'width="100%"' not in svg_str and "width='100%'" not in svg_str:
                            issues.append(f"[{file}] {q_id} image.svg missing width='100%'")
                        if 'height="100%"' not in svg_str and "height='100%'" not in svg_str:
                            issues.append(f"[{file}] {q_id} image.svg missing height='100%'")
                        if 'xmlns' not in svg_str:
                            issues.append(f"[{file}] {q_id} image.svg missing xmlns attribute")
                        if not svg_str.strip().endswith('</svg>'):
                            issues.append(f"[{file}] {q_id} image.svg does not end with '</svg>'")
                elif img_type == 'raster':
                    src = img.get('src', '')
                    if not isinstance(src, str) or len(src.strip()) == 0:
                        issues.append(f"[{file}] {q_id} image.src must be a non-empty string.")
                    else:
                        full_path = os.path.join(images_dir, src)
                        if not os.path.isfile(full_path):
                            issues.append(f"[{file}] {q_id} raster image not found: public/images/questions/{src}")
                # Validate alt text
                alt = img.get('alt')
                if not alt or not isinstance(alt, dict) or not alt.get('en'):
                    issues.append(f"[{file}] {q_id} image.alt must be an object with at least an 'en' key.")
        
        schema_error = False
        for lang, lang_data in [('en', en), ('kn', kn)]:
            opts = lang_data.get('options', [])
            
            # Helper to validate option structure and extract valid IDs/texts
            valid_option_values = []
            for i, opt in enumerate(opts):
                if isinstance(opt, dict):
                    if 'id' not in opt:
                        issues.append(f"[{file}] {q_id} {lang.upper()} option {i} missing 'id'.")
                        schema_error = True
                    else:
                        valid_option_values.append(opt['id'])
                    
                    if 'image' in opt:
                        img = opt['image']
                        if not isinstance(img, dict):
                            issues.append(f"[{file}] {q_id} {lang.upper()} option {i} 'image' must be an object.")
                            schema_error = True
                        else:
                            img_type = img.get('type')
                            if img_type not in ('svg', 'raster'):
                                issues.append(f"[{file}] {q_id} {lang.upper()} option {i} image.type must be 'svg' or 'raster'.")
                                schema_error = True
                            elif img_type == 'svg':
                                svg_str = img.get('svg', '')
                                if not isinstance(svg_str, str) or len(svg_str.strip()) == 0:
                                    issues.append(f"[{file}] {q_id} {lang.upper()} option {i} image.svg must be a non-empty string.")
                                    schema_error = True
                                else:
                                    if 'width="100%"' not in svg_str and "width='100%'" not in svg_str:
                                        issues.append(f"[{file}] {q_id} {lang.upper()} option {i} image.svg missing width='100%'")
                                        schema_error = True
                                    if 'height="100%"' not in svg_str and "height='100%'" not in svg_str:
                                        issues.append(f"[{file}] {q_id} {lang.upper()} option {i} image.svg missing height='100%'")
                                        schema_error = True
                                    if 'xmlns' not in svg_str:
                                        issues.append(f"[{file}] {q_id} {lang.upper()} option {i} image.svg missing xmlns attribute")
                                        schema_error = True
                                    if not svg_str.strip().endswith('</svg>'):
                                        issues.append(f"[{file}] {q_id} {lang.upper()} option {i} image.svg does not end with '</svg>'")
                                        schema_error = True
                else:
                    valid_option_values.append(opt)

            if effective_type == 'single':
                ans = lang_data.get('answer')
                if ans not in valid_option_values:
                    issues.append(f"[{file}] {q_id} {lang.upper()} answer not in options (or option IDs).")
                    schema_error = True
            elif effective_type == 'multiple':
                ans_list = lang_data.get('answer', [])
                if not isinstance(ans_list, list):
                    issues.append(f"[{file}] {q_id} {lang.upper()} answer must be a list for 'multiple' type.")
                    schema_error = True
                else:
                    for a in ans_list:
                        if a not in valid_option_values:
                            issues.append(f"[{file}] {q_id} {lang.upper()} answer '{a}' not in options (or option IDs).")
                            schema_error = True
            elif q_type == 'match':
                pairs = lang_data.get('pairs', [])
                if not isinstance(pairs, list) or len(pairs) == 0:
                    issues.append(f"[{file}] {q_id} {lang.upper()} must have a valid 'pairs' list for 'match' type.")
                    schema_error = True
                else:
                    for p in pairs:
                        if 'left' not in p or 'right' not in p:
                            issues.append(f"[{file}] {q_id} {lang.upper()} pair missing 'left' or 'right' keys.")
                            schema_error = True
                            
        if not schema_error:
            en_q_text = en.get('question', '').strip()
            # Precompute character counts for fuzzy check
            char_counts = Counter(en_q_text.lower())
            valid_questions.append({
                'text': en_q_text,
                'id': q_id,
                'file': file,
                'index': idx,
                'counter': char_counts
            })

    # 3. Exact Duplicate Checks (O(N) using a hash map)
    seen_exact = {}
    exact_duplicates_indices = set()
    for q in valid_questions:
        text = q['text']
        if text in seen_exact:
            seen_prev = seen_exact[text]
            issues.append(f"[{q['file']}] Exact Duplicate EN found: '{text}' (Matches {seen_prev['id']} in {seen_prev['file']})")
            exact_duplicates_indices.add(q['index'])
        else:
            seen_exact[text] = q

    # 4. Fuzzy Duplicate Checks (O(N log N) using sliding window on sorted lengths and L1 filter)
    fuzzy_candidates = [q for q in valid_questions if q['index'] not in exact_duplicates_indices]
    sorted_qs = sorted(fuzzy_candidates, key=lambda x: len(x['text']))
    
    n_candidates = len(sorted_qs)
    for i in range(n_candidates):
        q_i = sorted_qs[i]
        len_i = len(q_i['text'])
        if len_i == 0:
            continue
        c1 = q_i['counter']
            
        for j in range(i + 1, n_candidates):
            q_j = sorted_qs[j]
            len_j = len(q_j['text'])
            
            # Since sorted_qs is sorted by length, len_j >= len_i
            # If the ratio exceeds 1.11, we can stop searching for q_i
            if len_j / len_i > 1.11:
                break
                
            # Perform L1 character difference filter before running expensive similar()
            c2 = q_j['counter']
            all_chars = set(c1.keys()).union(c2.keys())
            l1_dist = sum(abs(c1.get(char, 0) - c2.get(char, 0)) for char in all_chars)
            upper_bound = 1.0 - l1_dist / (len_i + len_j)
            if upper_bound <= SIMILARITY_THRESHOLD:
                continue
                
            # Perform similarity check
            if similar(q_i['text'], q_j['text']) > SIMILARITY_THRESHOLD:
                first, second = (q_i, q_j) if q_i['index'] < q_j['index'] else (q_j, q_i)
                issues.append(f"[{second['file']}] Fuzzy Duplicate EN found: '{second['text']}' ~ '{first['text']}' (Matches {first['id']} in {first['file']})")

    if issues:
        print("\n=== Validation Failed! Found Issues: ===")
        for i in issues:
            print("-", i)
        return False
    else:
        print("\n=== Validation Passed! Zero duplicates found. Schema is perfect. ===")
        return True

if __name__ == "__main__":
    success = verify_db()
    if not success:
        exit(1)
