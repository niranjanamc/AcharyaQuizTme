import os
import json
import sys
from verify_db import similar, SIMILARITY_THRESHOLD, DATA_DIR

def import_data(class_dir, subject_dir, chapter_file, new_data_file):
    target_path = os.path.join(DATA_DIR, class_dir, subject_dir, chapter_file)
    
    if not os.path.exists(new_data_file):
        print(f"Error: Could not find new data file: {new_data_file}")
        return

    with open(new_data_file, 'r', encoding='utf-8') as f:
        new_qs = json.load(f)
        
    if not isinstance(new_qs, list):
        print("Error: New data must be a JSON array of questions.")
        return

    existing_qs = []
    # We must check against the ENTIRE DB for duplicates, not just the chapter
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            existing_qs.extend(data)
                except:
                    pass

    existing_texts = [q['en']['question'].strip().lower() for q in existing_qs if 'en' in q]

    valid_new_qs = []
    for q in new_qs:
        en_text = q['en']['question'].strip().lower()
        is_duplicate = False
        for ex_text in existing_texts:
            if en_text == ex_text or similar(en_text, ex_text) > SIMILARITY_THRESHOLD:
                is_duplicate = True
                print(f"Rejected Duplicate: '{q['en']['question']}' is too similar to existing DB question.")
                break
        
        if not is_duplicate:
            valid_new_qs.append(q)
            existing_texts.append(en_text)

    if not valid_new_qs:
        print("No valid unique questions to add.")
        return

    # Now append to target chapter
    chapter_data = []
    if os.path.exists(target_path):
        with open(target_path, 'r', encoding='utf-8') as f:
            chapter_data = json.load(f)
            
    chapter_data.extend(valid_new_qs)
    
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully added {len(valid_new_qs)} unique questions to {target_path}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python import_data.py <class_dir> <subject_dir> <chapter_file.json> <new_data.json>")
        print("Example: python import_data.py class_5 science fundamentals.json new_batch.json")
    else:
        import_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
