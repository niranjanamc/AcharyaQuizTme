import json
import os
import sys

# Ensure cms is in path
sys.path.append(os.path.dirname(__file__))
import svg_templates

def append_questions(file_path, new_qs):
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        
    # Remove existing ones with these IDs if script runs multiple times
    new_ids = {q['id'] for q in new_qs}
    questions = [q for q in questions if q['id'] not in new_ids]
    
    questions.extend(new_qs)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Added {len(new_qs)} questions to {file_path}")

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    
    # Class 5 Maths: Shapes and Angles
    math_file = os.path.join(root, 'src/data/questions/class_5/maths/shapes_angles.json')
    
    m_svg = {
        "id": "c5_math_sa_img_001",
        "type": "image_single",
        "difficulty": 1,
        "image": {
            "type": "svg",
            "svg": svg_templates.svg_to_json_string(svg_templates.angle_diagram(90, '∠ABC = 90°')).strip('"'),
            "alt": {
                "en": "An angle measuring 90 degrees",
                "kn": "90 ಡಿಗ್ರಿ ಅಳತೆಯ ಕೋನ"
            }
        },
        "en": {
            "question": "What type of angle is shown in the diagram?",
            "options": ["Acute Angle", "Right Angle", "Obtuse Angle", "Straight Angle"],
            "answer": "Right Angle",
            "reasoning": "An angle that measures exactly 90 degrees is called a Right Angle."
        },
        "kn": {
            "question": "ಚಿತ್ರದಲ್ಲಿ ಯಾವ ರೀತಿಯ ಕೋನವನ್ನು ತೋರಿಸಲಾಗಿದೆ?",
            "options": ["ಲಘು ಕೋನ", "ಲಂಬ ಕೋನ", "ವಿಶಾಲ ಕೋನ", "ಸರಳ ಕೋನ"],
            "answer": "ಲಂಬ ಕೋನ",
            "reasoning": "ನಿಖರವಾಗಿ 90 ಡಿಗ್ರಿ ಅಳತೆಯ ಕೋನವನ್ನು ಲಂಬ ಕೋನ ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ."
        }
    }
    
    m_raster = {
        "id": "c5_math_sa_img_002",
        "type": "image_single",
        "difficulty": 2,
        "image": {
            "type": "raster",
            "src": "class_5/maths/shapes_angles_img_002.png",
            "alt": {
                "en": "A wall clock showing exactly 3 o'clock",
                "kn": "ನಿಖರವಾಗಿ 3 ಗಂಟೆ ತೋರಿಸುವ ಗೋಡೆ ಗಡಿಯಾರ"
            }
        },
        "en": {
            "question": "What angle do the hour and minute hands of this clock make at 3 o'clock?",
            "options": ["60 degrees", "90 degrees", "120 degrees", "180 degrees"],
            "answer": "90 degrees",
            "reasoning": "At 3 o'clock, the minute hand is at 12 and the hour hand is at 3. They form a right angle, which is 90 degrees."
        },
        "kn": {
            "question": "ಈ ಗಡಿಯಾರದ ಗಂಟೆ ಮತ್ತು ನಿಮಿಷದ ಮುಳ್ಳುಗಳು 3 ಗಂಟೆಗೆ ಎಷ್ಟು ಡಿಗ್ರಿ ಕೋನವನ್ನು ಉಂಟುಮಾಡುತ್ತವೆ?",
            "options": ["60 ಡಿಗ್ರಿ", "90 ಡಿಗ್ರಿ", "120 ಡಿಗ್ರಿ", "180 ಡಿಗ್ರಿ"],
            "answer": "90 ಡಿಗ್ರಿ",
            "reasoning": "3 ಗಂಟೆಗೆ, ನಿಮಿಷದ ಮುಳ್ಳು 12 ರಲ್ಲಿದೆ ಮತ್ತು ಗಂಟೆಯ ಮುಳ್ಳು 3 ರಲ್ಲಿದೆ. ಅವು ಲಂಬ ಕೋನವನ್ನು ರೂಪಿಸುತ್ತವೆ, ಅಂದರೆ 90 ಡಿಗ್ರಿ."
        }
    }
    
    append_questions(math_file, [m_svg, m_raster])
    
    # Class 5 Science: Properties of Matter
    sci_file = os.path.join(root, 'src/data/questions/class_5/science/properties_matter.json')
    
    s_svg = {
        "id": "c5_sci_pm_img_001",
        "type": "image_single",
        "difficulty": 2,
        "image": {
            "type": "svg",
            "svg": svg_templates.svg_to_json_string(svg_templates.bar_chart([78, 21, 1], ['Nitrogen', 'Oxygen', 'Other'], title='Gases in Air')).strip('"'),
            "alt": {
                "en": "Bar chart showing Nitrogen 78, Oxygen 21, Other 1",
                "kn": "ಬಾರ್ ಚಾರ್ಟ್ ಸಾರಜನಕ 78, ಆಮ್ಲಜನಕ 21, ಇತರೆ 1 ತೋರಿಸುತ್ತಿದೆ"
            }
        },
        "en": {
            "question": "According to the chart, which gas makes up the largest part of the air we breathe?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Other"],
            "answer": "Nitrogen",
            "reasoning": "The tallest bar shows that Nitrogen makes up 78% of the air."
        },
        "kn": {
            "question": "ಚಾರ್ಟ್ ಪ್ರಕಾರ, ನಾವು ಉಸಿರಾಡುವ ಗಾಳಿಯಲ್ಲಿ ಯಾವ ಅನಿಲವು ದೊಡ್ಡ ಭಾಗವನ್ನು ಹೊಂದಿದೆ?",
            "options": ["ಆಮ್ಲಜನಕ", "ಸಾರಜನಕ", "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್", "ಇತರೆ"],
            "answer": "ಸಾರಜನಕ",
            "reasoning": "ಅತಿ ಎತ್ತರದ ಬಾರ್ ಗಾಳಿಯಲ್ಲಿ ಶೇಕಡಾ 78 ರಷ್ಟು ಸಾರಜನಕವಿದೆ ಎಂದು ತೋರಿಸುತ್ತದೆ."
        }
    }
    
    s_raster = {
        "id": "c5_sci_pm_img_002",
        "type": "image_single",
        "difficulty": 1,
        "image": {
            "type": "raster",
            "src": "class_5/science/properties_matter_img_002.png",
            "alt": {
                "en": "An ice cube melting into a puddle of water on a table",
                "kn": "ಮೇಜಿನ ಮೇಲೆ ಕರಗಿ ನೀರಿನ ಗುಂಡಿಯಾಗುತ್ತಿರುವ ಐಸ್ ಕ್ಯೂಬ್"
            }
        },
        "en": {
            "question": "What process is shown in the image where solid ice turns into liquid water?",
            "options": ["Freezing", "Melting", "Evaporation", "Condensation"],
            "answer": "Melting",
            "reasoning": "When a solid like ice absorbs heat and turns into a liquid, the process is called melting."
        },
        "kn": {
            "question": "ಘನ ಐಸ್ ದ್ರವ ನೀರಾಗಿ ಬದಲಾಗುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಚಿತ್ರದಲ್ಲಿ ತೋರಿಸಲಾಗಿದೆ, ಇದನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "options": ["ಘನೀಕರಣ", "ಕರಗುವಿಕೆ", "ಆವಿಯಾಗುವಿಕೆ", "ಸಾಂದ್ರೀಕರಣ"],
            "answer": "ಕರಗುವಿಕೆ",
            "reasoning": "ಐಸ್‌ನಂತಹ ಘನವಸ್ತುವು ಶಾಖವನ್ನು ಹೀರಿಕೊಂಡು ದ್ರವವಾಗಿ ಬದಲಾದಾಗ, ಆ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಕರಗುವಿಕೆ ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ."
        }
    }
    
    append_questions(sci_file, [s_svg, s_raster])

if __name__ == '__main__':
    main()
