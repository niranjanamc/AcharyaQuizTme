import os
import json

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'data', 'questions')

def fix_all():
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(root, file)
                modified = False
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                    except Exception as e:
                        print(f"Error loading {file}: {e}")
                        continue
                
                if not isinstance(data, list):
                    continue
                
                for q in data:
                    q_id = q.get('id')
                    q_type = q.get('type', 'single')
                    
                    # 1. Convert dictionary pairs to list format for match type
                    if q_type == 'match':
                        for lang in ['en', 'kn']:
                            if lang in q and 'pairs' in q[lang]:
                                pairs = q[lang]['pairs']
                                if isinstance(pairs, dict):
                                    new_pairs = [{"left": k, "right": v} for k, v in pairs.items()]
                                    q[lang]['pairs'] = new_pairs
                                    modified = True
                    
                    # 2. Specific Class 5 Mismatches
                    if q_id == 'c5_eng_unit1_022':
                        # Fix the "and" vs "ಮತ್ತು" typo in Kannada answer
                        q['kn']['answer'] = "ನಾವು ಸೃಜನಶೀಲರಾಗಿರಬೇಕು ಮತ್ತು ಮರುಬಳಕೆ ಮಾಡಬಹುದಾದ ವಸ್ತುಗಳನ್ನು ವ್ಯರ್ಥ ಮಾಡಬಾರದು"
                        modified = True
                    
                    if q_id == 'c5_eng_unit7_009':
                        # Convert list answer to string for single choice
                        if isinstance(q['kn']['answer'], list):
                            q['kn']['answer'] = q['kn']['answer'][0]
                            modified = True
                            
                    if q_id == 'c5_his_empires_019':
                        # Fix Kannada unicode mismatch in answer
                        q['kn']['answer'] = "ಕಾಳಿದಾಸ"
                        modified = True
                        
                    if q_id == 'c5_his_empires_022':
                        # Fix list answer mismatch
                        q['kn']['answer'] = ["ಆರ್ಯಭಟ", "ಕಾಳಿದಾಸ"]
                        modified = True
                        
                    if q_id == 'c5_his_humans_020':
                        # Fix the "and" vs "ಮತ್ತು" typo in Kannada answer
                        q['kn']['answer'] = "ಹೆಚ್ಚುವರಿ ಧಾನ್ಯಗಳನ್ನು ಸಂಗ್ರಹಿಸಲು ಮತ್ತು ಆಹಾರ ಬೇಯಿಸಲು"
                        modified = True
                        
                    if q_id == 'c5_kan_unit6_010':
                        # Convert list answer to string for single choice
                        if isinstance(q['kn']['answer'], list):
                            q['kn']['answer'] = q['kn']['answer'][0]
                            modified = True
                    
                    # 3. Class 5 Fuzzy Duplicates in Match Questions
                    if q_id == 'c5_eng_unit1_017':
                        q['en']['question'] = "Match the vocabulary words from Unit 1 (Ice-cream Man & Wonderful Waste) with their correct meanings:"
                        modified = True
                    if q_id == 'c5_eng_unit4_017':
                        q['en']['question'] = "Match the vocabulary words from Unit 4 (Crying & My Elder Brother) with their correct meanings:"
                        modified = True
                    if q_id == 'c5_eng_unit5_025':
                        q['en']['question'] = "Match the describing adjectives from Unit 5 (Rip Van Winkle & The Lazy Frog) with their corresponding nouns:"
                        modified = True
                    if q_id == 'c5_eng_unit1_025':
                        q['en']['question'] = "Match the describing adjectives from Unit 1 (Ice-cream Man) to their corresponding nouns:"
                        modified = True
                    
                    # 4. Class 6 Fuzzy Duplicates & Other fixes
                    if q_id == 'c6_math_pm_21':
                        q['en']['question'] = "Match the arithmetic sequence with its next term:"
                        modified = True
                    if q_id == 'c6_math_pm_33':
                        q['en']['question'] = "Match the arithmetic sequence with its missing middle term:"
                        modified = True
                    if q_id == 'c6_math_pt_20':
                        q['en']['question'] = "Identify the divisibility rule: A number is divisible by 5 if its last digit is:"
                        modified = True
                    if q_id == 'c6_math_pt_16':
                        q['en']['question'] = "Identify the divisibility rule: A number is divisible by 2 if its last digit is:"
                        modified = True
                    if q_id == 'c6_math_pt_38':
                        # Change 'Which of these are composite numbers?' to avoid duplication
                        q['en']['question'] = "Select all the composite numbers from the options below:"
                        modified = True
                    
                    # 5. Fix duplicate question IDs or exact duplicate questions in data_handling.json
                    if file == 'data_handling.json' and q_id == 'c6_math_dh_38_dup': # if we run multiple times
                        pass
                    
                if modified:
                    with open(path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    print(f"Fixed {file}")

if __name__ == "__main__":
    fix_all()
