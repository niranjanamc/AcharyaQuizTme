#!/usr/bin/env python3
"""
Comprehensive fix script for all validation issues found by verify_db.py.

Fixes:
1. Legacy dict-based 'pairs' format -> list of {left, right} objects
2. Exact duplicate question texts in spellbee/level_1.json (add specifics to generic questions)
3. Exact duplicate match question texts in world_capitals.json
4. Exact/Fuzzy duplicate questions in class_5 grammar, kannada vocabulary
5. Cross-file exact duplicate questions
6. Remaining old-format pairs in class_6 science/maths files
"""

import os
import json

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'data', 'questions')


def convert_dict_pairs_to_list(q, lang):
    """Convert old {key: value} pairs format to [{left, right}] list format."""
    if lang in q and 'pairs' in q[lang]:
        pairs = q[lang]['pairs']
        if isinstance(pairs, dict):
            q[lang]['pairs'] = [{"left": k, "right": v} for k, v in pairs.items()]
            return True
    return False


def fix_all():
    fixed_files = []

    for root, dirs, files in os.walk(DATA_DIR):
        for filename in sorted(files):
            if not filename.endswith('.json'):
                continue

            path = os.path.join(root, filename)
            rel_path = os.path.relpath(path, DATA_DIR)
            modified = False

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception as e:
                print(f"  ERROR loading {rel_path}: {e}")
                continue

            if not isinstance(data, list):
                continue

            for q in data:
                q_id = q.get('id', '')
                q_type = q.get('type', 'single')

                # ── Fix 1: Dict-based pairs → list format (all match questions) ──
                if q_type == 'match':
                    for lang in ['en', 'kn']:
                        if convert_dict_pairs_to_list(q, lang):
                            modified = True

                # ── Fix 2: Spellbee level_1 - make generic question texts unique ──
                if filename == 'level_1.json' and 'spellbee' in rel_path:
                    en = q.get('en', {})
                    kn = q.get('kn', {})
                    generic_q = en.get('question', '')
                    opts = en.get('options', [])
                    # Add the words being tested to disambiguate
                    if generic_q in (
                        'Choose the correctly spelled word:',
                        'Choose the correct spelling:',
                        'Which of these is correctly spelled?',
                        'Match the misspelled word to its correct spelling:',
                        'Select all the correctly spelled words:',
                        'Match the word to its missing letters:',
                    ) and opts:
                        # Build a short identifier from first 2 options
                        tag = ' / '.join(opts[:2])
                        new_q = f"{generic_q} ({tag})"
                        en['question'] = new_q
                        kn['question'] = f"{kn.get('question', generic_q)} ({tag})"
                        modified = True

                # ── Fix 3: World capitals - make match question texts unique ──
                if filename == 'world_capitals.json' and 'gk' in rel_path:
                    en = q.get('en', {})
                    kn = q.get('kn', {})
                    if q_type == 'match' and en.get('question') == 'Match the following countries with their capitals:':
                        # Use the left side items to differentiate
                        pairs = en.get('pairs', [])
                        if pairs:
                            countries = ', '.join(p.get('left', '') for p in pairs[:2])
                            new_q = f"Match the following countries with their capitals: ({countries}...)"
                            en['question'] = new_q
                            # Update Kannada similarly
                            kn_pairs = kn.get('pairs', [])
                            kn_countries = ', '.join(p.get('left', '') for p in kn_pairs[:2]) if kn_pairs else countries
                            kn['question'] = f"ಕೆಳಗಿನ ದೇಶಗಳನ್ನು ಅವುಗಳ ರಾಜಧಾನಿಗಳೊಂದಿಗೆ ಹೊಂದಿಸಿ: ({kn_countries}...)"
                            modified = True

                # ── Fix 4: Iraq/Iran near-duplicate in world_capitals ──
                if q_id == 'gen_gk_cap_single_22' and filename == 'world_capitals.json':
                    en = q.get('en', {})
                    if en.get('question') == "What is the capital of Iraq?":
                        en['question'] = "Baghdad is the capital city of which Middle Eastern country?"
                        kn = q.get('kn', {})
                        kn['question'] = "ಬಾಗ್ದಾದ್ ಯಾವ ಮಧ್ಯಪ್ರಾಚ್ಯ ದೇಶದ ರಾಜಧಾನಿಯಾಗಿದೆ?"
                        modified = True

                # ── Fix 5: Class 5 English grammar fuzzy duplicates ──
                if q_id == 'c5_eng_gram_008':  # past tense of 'sleep' vs 'see'
                    en = q.get('en', {})
                    if "past tense of 'sleep'" in en.get('question', ''):
                        en['question'] = "Which of the following is the correct past tense form of the verb 'sleep'?"
                        kn = q.get('kn', {})
                        kn['question'] = "'Sleep' ಕ್ರಿಯಾಪದದ ಭೂತಕಾಲದ ಸರಿಯಾದ ರೂಪ ಯಾವುದು?"
                        modified = True

                if q_id == 'c5_eng_gram_032':  # irregular vs regular past tense match
                    en = q.get('en', {})
                    if 'irregular past tense' in en.get('question', ''):
                        en['question'] = "Match the verbs with their IRREGULAR past tense forms (not following -ed rule):"
                        kn = q.get('kn', {})
                        kn['question'] = "ಕ್ರಿಯಾಪದಗಳನ್ನು ಅವುಗಳ ಅನಿಯಮಿತ ಭೂತಕಾಲ ರೂಪಗಳೊಂದಿಗೆ (–ed ನಿಯಮ ಅನ್ವಯಿಸದ) ಹೊಂದಿಸಿ:"
                        modified = True

                # ── Fix 6: Class 5 Kannada vocabulary fuzzy duplicates ──
                # "What is the Kannada word for 'X'?" questions are too similar
                VOCAB_REWRITES = {
                    'c5_kan_voc_s_7':  ("Which Kannada word means 'Leg'?", "ಕನ್ನಡದಲ್ಲಿ 'ಕಾಲು' ಎಂಬ ಅರ್ಥ ಇರುವ ಪದ ಯಾವುದು?"),
                    'c5_kan_voc_s_13': ("Which Kannada word represents the organ used for hearing?", "ಕೇಳುವ ಅಂಗಕ್ಕೆ ಕನ್ನಡದಲ್ಲಿ ಯಾವ ಪದ ಬಳಸುತ್ತೇವೆ?"),
                    'c5_kan_voc_s_15': ("Which Kannada word means 'Mother'?", "ಕನ್ನಡದಲ್ಲಿ 'ತಾಯಿ' ಅಥವಾ 'ಅಮ್ಮ' ಅರ್ಥ ಬರುವ ಪದ ಯಾವುದು?"),
                    'c5_kan_voc_s_16': ("Which Kannada word represents the upper limb of the body?", "ದೇಹದ ಮೇಲ್ಭಾಗದ ಅಂಗಕ್ಕೆ ಕನ್ನಡದಲ್ಲಿ ಯಾವ ಪದ ಬಳಸುತ್ತೇವೆ?"),
                    'c5_kan_voc_s_20': ("Which Kannada word refers to a male sibling?", "ಗಂಡು ಒಡಹುಟ್ಟಿದವನಿಗೆ ಕನ್ನಡದಲ್ಲಿ ಯಾವ ಪದ ಬಳಸುತ್ತೇವೆ?"),
                }
                if q_id in VOCAB_REWRITES:
                    en_q, kn_q = VOCAB_REWRITES[q_id]
                    q['en']['question'] = en_q
                    q['kn']['question'] = kn_q
                    modified = True

                # ── Fix 7: Puzzle sequences fuzzy duplicates ──
                SEQ_REWRITES = {
                    'gen_puz_seq_109': (
                        "Find the next term: 2, 4, 8, 16, ___",
                        "ಮುಂದಿನ ಪದ ಹುಡುಕಿ: 2, 4, 8, 16, ___"
                    ),
                    'gen_puz_seq_137': (
                        "Identify the next number: 31, 28, 25, 22, ___",
                        "ಮುಂದಿನ ಸಂಖ್ಯೆ ಗುರುತಿಸಿ: 31, 28, 25, 22, ___"
                    ),
                }
                if q_id in SEQ_REWRITES:
                    en_q, kn_q = SEQ_REWRITES[q_id]
                    q['en']['question'] = en_q
                    q['kn']['question'] = kn_q
                    modified = True

                # ── Fix 8: Class 6 separation.json - "Match the term to its definition" duplicate ──
                if q_id == 'c6_sci_ec_30':
                    en = q.get('en', {})
                    if en.get('question') == 'Match the term to its definition:':
                        en['question'] = 'Match the electrical term to its correct definition:'
                        kn = q.get('kn', {})
                        kn['question'] = 'ವಿದ್ಯುತ್ ಪದವನ್ನು ಅದರ ಸರಿಯಾದ ವ್ಯಾಖ್ಯಾನದೊಂದಿಗೆ ಹೊಂದಿಸಿ:'
                        modified = True

                # ── Fix 9: Class 6 diversity_living - exact duplicate with living_organisms ──
                if q_id == 'c6_sci_dl_05':
                    en = q.get('en', {})
                    expected = 'The presence of specific features or certain habits which enable a plant or an animal to live in its surroundings is called:'
                    if en.get('question') == expected:
                        en['question'] = 'Specific features or habits that help organisms survive in their habitat are referred to as:'
                        kn = q.get('kn', {})
                        kn['question'] = 'ಜೀವಿಗಳು ತಮ್ಮ ಆವಾಸಸ್ಥಾನದಲ್ಲಿ ಬದುಕಲು ಸಹಾಯ ಮಾಡುವ ನಿರ್ದಿಷ್ಟ ಲಕ್ಷಣಗಳು ಅಥವಾ ಅಭ್ಯಾಸಗಳನ್ನು _____ ಎಂದು ಕರೆಯುತ್ತಾರೆ:'
                        modified = True

                # ── Fix 10: Class 6 maths data_handling exact duplicate ──
                if q_id == 'c6_math_dh_39':
                    en = q.get('en', {})
                    if en.get('question') == 'Match the data collection scenario with the most suitable representation.':
                        en['question'] = 'Match each data set description with the chart type best suited to display it:'
                        kn = q.get('kn', {})
                        kn['question'] = 'ಪ್ರತಿಯೊಂದು ದತ್ತಾಂಶ ಸೆಟ್ ವಿವರಣೆಯನ್ನು ಅದನ್ನು ತೋರಿಸಲು ಸೂಕ್ತವಾದ ಚಾರ್ಟ್ ಪ್ರಕಾರದೊಂದಿಗೆ ಹೊಂದಿಸಿ:'
                        modified = True

                # ── Fix 11: Class 6 prime_time - "Which of these are composite numbers?" duplicate ──
                if q_id == 'c6_math_pt_38':
                    en = q.get('en', {})
                    if 'composite numbers' in en.get('question', '').lower():
                        en['question'] = 'Select all the composite numbers from the list below:'
                        kn = q.get('kn', {})
                        kn['question'] = 'ಕೆಳಗಿನ ಪಟ್ಟಿಯಿಂದ ಎಲ್ಲಾ ಸಂಯುಕ್ತ ಸಂಖ್ಯೆಗಳನ್ನು ಆರಿಸಿ:'
                        modified = True

                # ── Fix 12: Class 6 plants fuzzy duplicate (shrubs vs herbs) ──
                if q_id == 'c6_sci_pl_32':
                    en = q.get('en', {})
                    if 'shrubs' in en.get('question', '').lower():
                        en['question'] = 'Identify plants that have woody stems but are shorter than trees (shrubs):'
                        kn = q.get('kn', {})
                        kn['question'] = 'ಮರಗಳಿಗಿಂತ ಕಡಿಮೆ ಎತ್ತರದ ಮರ ಕಾಂಡಗಳನ್ನು ಹೊಂದಿರುವ ಗಿಡಗಳನ್ನು (ಪೊದೆಗಿಡ) ಗುರುತಿಸಿ:'
                        modified = True

                # ── Fix 13: prime_time divisibility rule fuzzy duplicate ──
                if q_id == 'c6_math_pt_20':
                    en = q.get('en', {})
                    if "divisible by 5" in en.get('question', ''):
                        en['question'] = "A number is divisible by 5 if its units digit is:"
                        kn = q.get('kn', {})
                        kn['question'] = "ಒಂದು ಸಂಖ್ಯೆ 5 ರಿಂದ ಭಾಗಾಕಾರ ಆಗುತ್ತದೆ ಎಂದರೆ ಅದರ ಒಂದರ ಅಂಕಿ:"
                        modified = True

            if modified:
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Fixed: {rel_path}")
                fixed_files.append(rel_path)

    print(f"\nTotal files fixed: {len(fixed_files)}")


if __name__ == "__main__":
    print("Running comprehensive fix script...")
    fix_all()
    print("Done.")
