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
        
        schema_error = False
        for lang, lang_data in [('en', en), ('kn', kn)]:
            if q_type == 'single':
                if lang_data.get('answer') not in lang_data.get('options', []):
                    issues.append(f"[{file}] {q_id} {lang.upper()} answer not in options.")
                    schema_error = True
            elif q_type == 'multiple':
                ans_list = lang_data.get('answer', [])
                if not isinstance(ans_list, list):
                    issues.append(f"[{file}] {q_id} {lang.upper()} answer must be a list for 'multiple' type.")
                    schema_error = True
                else:
                    opts = lang_data.get('options', [])
                    for a in ans_list:
                        if a not in opts:
                            issues.append(f"[{file}] {q_id} {lang.upper()} answer '{a}' not in options.")
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
