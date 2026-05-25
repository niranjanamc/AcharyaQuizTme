import json

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old_text, new_text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/science'

replace_in_file(f'{base_dir}/physical_chemical_changes.json', 
                '"question": "Which of the following are examples of chemical changes?"', 
                '"question": "Which of these represent examples of chemical changes?"')

replace_in_file(f'{base_dir}/wastewater.json', 
                '"question": "Match the term with its meaning:"', 
                '"question": "Match the wastewater term with its meaning:"')

replace_in_file(f'{base_dir}/reproduction_plants.json', 
                '"question": "What is the female reproductive part of a flower called?"', 
                '"question": "Identify the female reproductive part of a flower."')

print("Fixed duplicates")
