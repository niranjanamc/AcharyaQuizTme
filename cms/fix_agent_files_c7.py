import os
import json
import glob

def get_letter(idx):
    return chr(65 + idx)

def fix_english(data):
    new_data = []
    for idx, q in enumerate(data):
        try:
            # Check if already correct
            if 'en' in q and 'question' in q['en'] and 'options' in q['en']:
                new_data.append(q)
                continue
                
            q_type = q.get('type', 'single')
            
            # Extract common
            q_id = q.get('id', f'c7_eng_un_{idx}')
            difficulty = q.get('difficulty', 'medium')
            q_en = q.get('question', {}).get('en', '')
            q_kn = q.get('question', {}).get('kn', '')
            exp_en = q.get('explanation', {}).get('en', '')
            exp_kn = q.get('explanation', {}).get('kn', '')

            new_q = {
                "id": q_id,
                "type": q_type,
                "difficulty": difficulty,
                "en": { "question": q_en },
                "kn": { "question": q_kn }
            }

            if exp_en: new_q["en"]["explanation"] = exp_en
            if exp_kn: new_q["kn"]["explanation"] = exp_kn

            if q_type in ('single', 'multiple'):
                opts_en = []
                opts_kn = []
                # Check how options are formatted
                if isinstance(q.get('options'), dict) and 'en' in q['options']:
                    # English writer format
                    ans = q.get('correctAnswer')
                    if isinstance(ans, list):
                        correct_indices = set(ans)
                    else:
                        correct_indices = {ans} if isinstance(ans, int) else set()

                    en_list = q['options']['en']
                    kn_list = q['options']['kn']
                    
                    for i, (te, tk) in enumerate(zip(en_list, kn_list)):
                        is_corr = i in correct_indices
                        opts_en.append({"id": get_letter(i), "text": te, "isCorrect": is_corr})
                        opts_kn.append({"id": get_letter(i), "text": tk, "isCorrect": is_corr})
                
                new_q["en"]["options"] = opts_en
                new_q["kn"]["options"] = opts_kn
                
            elif q_type == 'match':
                opts_en = []
                opts_kn = []
                # Match questions in english writer
                options = q.get('options', {})
                matchOptions = q.get('matchOptions', {})
                
                en_left = options.get('en', [])
                kn_left = options.get('kn', [])
                en_right = matchOptions.get('en', [])
                kn_right = matchOptions.get('kn', [])
                ans = q.get('correctAnswer', {})
                
                for i, (l_en, l_kn) in enumerate(zip(en_left, kn_left)):
                    r_idx = ans.get(str(i), i)
                    if isinstance(r_idx, int) and r_idx < len(en_right):
                        r_en = en_right[r_idx]
                        r_kn = kn_right[r_idx]
                    else:
                        r_en, r_kn = "",""
                    
                    opts_en.append({"id": get_letter(i), "left": l_en, "right": r_en})
                    opts_kn.append({"id": get_letter(i), "left": l_kn, "right": r_kn})
                
                new_q["en"]["options"] = opts_en
                new_q["kn"]["options"] = opts_kn

            new_data.append(new_q)
        except Exception as e:
            print(f"Error fixing {q.get('id')} in English: {e}")
            new_data.append(q) # fallback
    return new_data


def fix_history(data):
    new_data = []
    for idx, q in enumerate(data):
        try:
            # Check if already correct
            if 'en' in q and 'question' in q['en'] and 'options' in q['en']:
                new_data.append(q)
                continue
                
            q_type = q.get('type', 'single')
            
            # Extract common
            q_id = q.get('id', f'c7_his_un_{idx}')
            difficulty = q.get('difficulty', 'medium')
            q_en = q.get('question', {}).get('en', '')
            q_kn = q.get('question', {}).get('kn', '')

            new_q = {
                "id": q_id,
                "type": q_type,
                "difficulty": difficulty,
                "en": { "question": q_en },
                "kn": { "question": q_kn }
            }

            if q_type in ('single', 'multiple'):
                opts_en = []
                opts_kn = []
                options = q.get('options', [])
                for i, opt in enumerate(options):
                    is_corr = opt.get('isCorrect', False)
                    opts_en.append({"id": get_letter(i), "text": opt.get('en', ''), "isCorrect": is_corr})
                    opts_kn.append({"id": get_letter(i), "text": opt.get('kn', ''), "isCorrect": is_corr})
                
                new_q["en"]["options"] = opts_en
                new_q["kn"]["options"] = opts_kn
                
            elif q_type == 'match':
                opts_en = []
                opts_kn = []
                pairs = q.get('pairs', [])
                for i, p in enumerate(pairs):
                    l_en = p.get('left', {}).get('en', '')
                    l_kn = p.get('left', {}).get('kn', '')
                    r_en = p.get('right', {}).get('en', '')
                    r_kn = p.get('right', {}).get('kn', '')
                    
                    opts_en.append({"id": get_letter(i), "left": l_en, "right": r_en})
                    opts_kn.append({"id": get_letter(i), "left": l_kn, "right": r_kn})
                
                new_q["en"]["options"] = opts_en
                new_q["kn"]["options"] = opts_kn

            new_data.append(new_q)
        except Exception as e:
            print(f"Error fixing {q.get('id')} in History: {e}")
            new_data.append(q)
    return new_data


def fix_kannada(data):
    new_data = []
    for idx, q in enumerate(data):
        try:
            # Check if already correct
            if 'en' in q and 'question' in q['en'] and 'options' in q['en']:
                new_data.append(q)
                continue
                
            q_type = q.get('type', 'single')
            
            # Extract common
            q_id = q.get('id', f'c7_kan_un_{idx}')
            difficulty = q.get('difficulty', 'medium')
            q_en = q.get('question', {}).get('en', '')
            q_kn = q.get('question', {}).get('kn', '')

            new_q = {
                "id": q_id,
                "type": q_type,
                "difficulty": difficulty,
                "en": { "question": q_en },
                "kn": { "question": q_kn }
            }

            if q_type in ('single', 'multiple'):
                opts_en = []
                opts_kn = []
                options = q.get('options', [])
                for i, opt in enumerate(options):
                    is_corr = opt.get('isCorrect', False)
                    t_en = opt.get('text', {}).get('en', '')
                    t_kn = opt.get('text', {}).get('kn', '')
                    opts_en.append({"id": get_letter(i), "text": t_en, "isCorrect": is_corr})
                    opts_kn.append({"id": get_letter(i), "text": t_kn, "isCorrect": is_corr})
                
                new_q["en"]["options"] = opts_en
                new_q["kn"]["options"] = opts_kn
                
            elif q_type == 'match':
                opts_en = []
                opts_kn = []
                pairs = q.get('pairs', [])
                for i, p in enumerate(pairs):
                    l_en = p.get('left', {}).get('en', '')
                    l_kn = p.get('left', {}).get('kn', '')
                    r_en = p.get('right', {}).get('en', '')
                    r_kn = p.get('right', {}).get('kn', '')
                    
                    opts_en.append({"id": get_letter(i), "left": l_en, "right": r_en})
                    opts_kn.append({"id": get_letter(i), "left": l_kn, "right": r_kn})
                
                new_q["en"]["options"] = opts_en
                new_q["kn"]["options"] = opts_kn

            new_data.append(new_q)
        except Exception as e:
            print(f"Error fixing {q.get('id')} in Kannada: {e}")
            new_data.append(q)
    return new_data


def process_files(dir_path, fix_func):
    for fpath in glob.glob(os.path.join(dir_path, '*.json')):
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fixed_data = fix_func(data)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(fixed_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    base_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7'
    
    eng_dir = os.path.join(base_dir, 'english')
    his_dir = os.path.join(base_dir, 'history')
    kan_dir = os.path.join(base_dir, 'kannada')
    
    process_files(eng_dir, fix_english)
    print("Fixed English")
    
    process_files(his_dir, fix_history)
    print("Fixed History")
    
    process_files(kan_dir, fix_kannada)
    print("Fixed Kannada")

