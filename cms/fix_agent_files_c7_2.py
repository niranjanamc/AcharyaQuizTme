import os
import json
import glob

def get_letter(idx):
    return chr(65 + idx)

def set_answers(lang_data, q_type):
    if q_type == 'single':
        for opt in lang_data.get('options', []):
            if opt.get('isCorrect'):
                lang_data['answer'] = opt.get('id')
                break
    elif q_type == 'multiple':
        ans_list = []
        for opt in lang_data.get('options', []):
            if opt.get('isCorrect'):
                ans_list.append(opt.get('id'))
        lang_data['answer'] = ans_list

def ensure_schema(q, data):
    new_q = q.copy()
    q_type = new_q.get('type')
    
    # Fix pairs for match
    if q_type == 'match':
        for lang in ['en', 'kn']:
            if lang in new_q and 'options' in new_q[lang]:
                # In match questions, we should use 'pairs' not 'options'
                pairs = []
                for opt in new_q[lang]['options']:
                    pairs.append({
                        "left": opt.get('left', ''),
                        "right": opt.get('right', '')
                    })
                new_q[lang]['pairs'] = pairs
                del new_q[lang]['options']
    else:
        # Set answers for single/multiple
        for lang in ['en', 'kn']:
            if lang in new_q:
                set_answers(new_q[lang], q_type)
                
    return new_q

def process_files(dir_path):
    for fpath in glob.glob(os.path.join(dir_path, '*.json')):
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fixed_data = []
        for q in data:
            fixed_data.append(ensure_schema(q, data))
        
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(fixed_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    base_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7'
    
    eng_dir = os.path.join(base_dir, 'english')
    his_dir = os.path.join(base_dir, 'history')
    kan_dir = os.path.join(base_dir, 'kannada')
    
    process_files(eng_dir)
    print("Fixed English Phase 2")
    
    process_files(his_dir)
    print("Fixed History Phase 2")
    
    process_files(kan_dir)
    print("Fixed Kannada Phase 2")
