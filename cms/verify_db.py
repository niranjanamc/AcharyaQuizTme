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
        
        if en.get('answer') not in en.get('options', []):
            issues.append(f"[{file}] {q_id} EN answer not in options.")
        if kn.get('answer') not in kn.get('options', []):
            issues.append(f"[{file}] {q_id} KN answer not in options.")
            
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
