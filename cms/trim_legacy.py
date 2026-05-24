import os
import json
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'data', 'questions')

FILES_TO_TRIM = [
    'class_5/maths/basic_operations.json',
    'general/puzzles/sequences.json'
]

# Max questions to keep per difficulty level per file
MAX_PER_DIFF = 3

def trim_legacy():
    for rel_path in FILES_TO_TRIM:
        path = os.path.join(DATA_DIR, rel_path)
        if not os.path.exists(path):
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            continue
            
        # Group by difficulty
        diff_groups = defaultdict(list)
        for q in data:
            diff = q.get('difficulty', 1)
            diff_groups[diff].append(q)
            
        trimmed_data = []
        for diff in sorted(diff_groups.keys()):
            # Keep only a small representative sample
            trimmed_data.extend(diff_groups[diff][:MAX_PER_DIFF])
            
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(trimmed_data, f, indent=2, ensure_ascii=False)
            
        print(f"Trimmed {rel_path}: from {len(data)} down to {len(trimmed_data)} structurally unique questions.")

if __name__ == "__main__":
    trim_legacy()
