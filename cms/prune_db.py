import os
import json
from verify_db import similar, SIMILARITY_THRESHOLD, DATA_DIR

def prune_db():
    total_pruned = 0
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if not isinstance(data, list):
                        continue
                        
                    seen_texts = []
                    unique_data = []
                    
                    for q in data:
                        if 'en' not in q:
                            unique_data.append(q)
                            continue
                            
                        en_text = q['en']['question'].strip().lower()
                        
                        is_dup = False
                        for seen in seen_texts:
                            if en_text == seen or similar(en_text, seen) > SIMILARITY_THRESHOLD:
                                is_dup = True
                                break
                                
                        if not is_dup:
                            unique_data.append(q)
                            seen_texts.append(en_text)
                        else:
                            total_pruned += 1
                            
                    if len(unique_data) < len(data):
                        with open(path, 'w', encoding='utf-8') as f:
                            json.dump(unique_data, f, indent=2, ensure_ascii=False)
                            
                except Exception as e:
                    print(f"Error on {file}: {e}")

    print(f"Pruning complete. Removed {total_pruned} duplicate questions.")

if __name__ == "__main__":
    prune_db()
