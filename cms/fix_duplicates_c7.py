import json

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old_text, new_text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_eng = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/english'
base_his = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/history'
base_kan = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/kannada'

# English
replace_in_file(f'{base_eng}/c7_eng_chappals.json', 
                '"Match the words with their meanings."', 
                '"Match the Chappals story words with their meanings."')

replace_in_file(f'{base_eng}/c7_eng_quality.json', 
                '"Match the words with their meanings."', 
                '"Match the Quality chapter words with their meanings."')

replace_in_file(f'{base_eng}/c7_eng_questions.json', 
                '"Match the characters with their descriptions."', 
                '"Match the characters from Three Questions with their descriptions."')

replace_in_file(f'{base_eng}/c7_eng_questions.json', 
                '"Match the words with their meanings."', 
                '"Match the vocabulary words with their meanings."')

# History
replace_in_file(f'{base_his}/c7_his_kings.json', 
                '"Match the terms with their meanings:"', 
                '"Match the historical terms with their meanings:"')

# Kannada
replace_in_file(f'{base_kan}/c7_kan_sailor.json', 
                '"Match the words with their meanings"', 
                '"Match the sailor words with their meanings"')

replace_in_file(f'{base_kan}/c7_kan_exam.json', 
                '"Match the words with their meanings"', 
                '"Match the examination words with their meanings"')

replace_in_file(f'{base_kan}/c7_kan_freedom.json', 
                '"Match the words with their meanings"', 
                '"Match the freedom song words with their meanings"')

replace_in_file(f'{base_kan}/c7_kan_puttajji.json', 
                '"Match the characters with their descriptions"', 
                '"Match the Puttajji characters with their descriptions"')

print("Fixed duplicates")
