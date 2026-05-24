import os
import json
from difflib import SequenceMatcher

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

    # 2. Schema Validation & Exact/Fuzzy Duplicate Checking
    seen_en_texts = []
    seen_kn_texts = []
    
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
        
        for lang, lang_data in [('en', en), ('kn', kn)]:
            if q_type == 'single':
                if lang_data.get('answer') not in lang_data.get('options', []):
                    issues.append(f"[{file}] {q_id} {lang.upper()} answer not in options.")
            elif q_type == 'multiple':
                ans_list = lang_data.get('answer', [])
                if not isinstance(ans_list, list):
                    issues.append(f"[{file}] {q_id} {lang.upper()} answer must be a list for 'multiple' type.")
                else:
                    opts = lang_data.get('options', [])
                    for a in ans_list:
                        if a not in opts:
                            issues.append(f"[{file}] {q_id} {lang.upper()} answer '{a}' not in options.")
            elif q_type == 'match':
                pairs = lang_data.get('pairs', [])
                if not isinstance(pairs, list) or len(pairs) == 0:
                    issues.append(f"[{file}] {q_id} {lang.upper()} must have a valid 'pairs' list for 'match' type.")
                else:
                    for p in pairs:
                        if 'left' not in p or 'right' not in p:
                            issues.append(f"[{file}] {q_id} {lang.upper()} pair missing 'left' or 'right' keys.")
            
        en_q_text = en.get('question', '').strip()
        kn_q_text = kn.get('question', '').strip()
        
        # Duplicate Checks
        for seen in seen_en_texts:
            if en_q_text == seen['text']:
                issues.append(f"[{file}] Exact Duplicate EN found: '{en_q_text}' (Matches {seen['id']} in {seen['file']})")
            elif similar(en_q_text, seen['text']) > SIMILARITY_THRESHOLD:
                issues.append(f"[{file}] Fuzzy Duplicate EN found: '{en_q_text}' ~ '{seen['text']}' (Matches {seen['id']} in {seen['file']})")
                
        seen_en_texts.append({'text': en_q_text, 'id': q_id, 'file': file})

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
