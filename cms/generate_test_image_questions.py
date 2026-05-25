import json
import os
import sys

# Ensure cms is in path so we can import svg_templates
sys.path.append(os.path.dirname(__file__))
import svg_templates

def main():
    questions_file = os.path.join(os.path.dirname(__file__), '../src/data/questions/class_6/maths/perimeter_area.json')
    
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        
    # Generate some image questions
    
    # 1. Image single with image options
    q1 = {
        "id": "c6_math_pa_img_001",
        "type": "image_single",
        "difficulty": 1,
        "image": {
            "type": "svg",
            "svg": svg_templates.svg_to_json_string(svg_templates.rectangle(12, 5, 'cm', ('A','B','C','D'))).strip('"'),
            "alt": {
                "en": "Rectangle with length 12 cm and width 5 cm",
                "kn": "ಉದ್ದ 12 ಸೆಂ.ಮೀ ಮತ್ತು ಅಗಲ 5 ಸೆಂ.ಮೀ ಇರುವ ಆಯತ"
            }
        },
        "en": {
            "question": "What is the area of the rectangle shown above?",
            "options": ["17 sq cm", "34 sq cm", "60 sq cm", "120 sq cm"],
            "answer": "60 sq cm",
            "reasoning": "Area of rectangle = length × width = 12 × 5 = 60 sq cm."
        },
        "kn": {
            "question": "ಮೇಲೆ ತೋರಿಸಿರುವ ಆಯತದ ವಿಸ್ತೀರ್ಣ ಎಷ್ಟು?",
            "options": ["17 ಚ.ಸೆಂ.ಮೀ", "34 ಚ.ಸೆಂ.ಮೀ", "60 ಚ.ಸೆಂ.ಮೀ", "120 ಚ.ಸೆಂ.ಮೀ"],
            "answer": "60 ಚ.ಸೆಂ.ಮೀ",
            "reasoning": "ಆಯತದ ವಿಸ್ತೀರ್ಣ = ಉದ್ದ × ಅಗಲ = 12 × 5 = 60 ಚ.ಸೆಂ.ಮೀ."
        }
    }
    
    # 2. Image multiple
    q2 = {
        "id": "c6_math_pa_img_002",
        "type": "image_multiple",
        "difficulty": 2,
        "image": {
            "type": "svg",
            "svg": svg_templates.svg_to_json_string(svg_templates.square(8, 'cm')).strip('"'),
            "alt": {
                "en": "Square with side length 8 cm",
                "kn": "ಬದಿಯ ಉದ್ದ 8 ಸೆಂ.ಮೀ ಇರುವ ಚೌಕ"
            }
        },
        "en": {
            "question": "Which of the following statements are true about the square above?",
            "options": [
                "Perimeter is 32 cm",
                "Area is 64 sq cm",
                "Perimeter is 64 cm",
                "Area is 32 sq cm"
            ],
            "answer": ["Perimeter is 32 cm", "Area is 64 sq cm"],
            "reasoning": "Perimeter = 4 × side = 4 × 8 = 32 cm. Area = side × side = 8 × 8 = 64 sq cm."
        },
        "kn": {
            "question": "ಮೇಲಿನ ಚೌಕದ ಬಗ್ಗೆ ಕೆಳಗಿನ ಯಾವ ಹೇಳಿಕೆಗಳು ನಿಜ?",
            "options": [
                "ಸುತ್ತಳತೆ 32 ಸೆಂ.ಮೀ",
                "ವಿಸ್ತೀರ್ಣ 64 ಚ.ಸೆಂ.ಮೀ",
                "ಸುತ್ತಳತೆ 64 ಸೆಂ.ಮೀ",
                "ವಿಸ್ತೀರ್ಣ 32 ಚ.ಸೆಂ.ಮೀ"
            ],
            "answer": ["ಸುತ್ತಳತೆ 32 ಸೆಂ.ಮೀ", "ವಿಸ್ತೀರ್ಣ 64 ಚ.ಸೆಂ.ಮೀ"],
            "reasoning": "ಸುತ್ತಳತೆ = 4 × ಬದಿ = 4 × 8 = 32 ಸೆಂ.ಮೀ. ವಿಸ್ತೀರ್ಣ = ಬದಿ × ಬದಿ = 8 × 8 = 64 ಚ.ಸೆಂ.ಮೀ."
        }
    }
    
    # 3. Image options question
    q3 = {
        "id": "c6_math_pa_img_003",
        "type": "image_single",
        "difficulty": 1,
        "en": {
            "question": "Which of these shapes has the largest perimeter?",
            "options": [
                {
                    "id": "optA",
                    "text": "Square (Side=4cm)",
                    "image": {
                        "type": "svg",
                        "svg": svg_templates.svg_to_json_string(svg_templates.square(4, 'cm')).strip('"'),
                        "alt": {"en": "Square with side 4 cm", "kn": "4 ಸೆಂ.ಮೀ ಬದಿಯಿರುವ ಚೌಕ"}
                    }
                },
                {
                    "id": "optB",
                    "text": "Rectangle (7cm × 3cm)",
                    "image": {
                        "type": "svg",
                        "svg": svg_templates.svg_to_json_string(svg_templates.rectangle(7, 3, 'cm')).strip('"'),
                        "alt": {"en": "Rectangle with sides 7 cm and 3 cm", "kn": "7 ಸೆಂ.ಮೀ ಮತ್ತು 3 ಸೆಂ.ಮೀ ಬದಿಗಳ ಆಯತ"}
                    }
                },
                {
                    "id": "optC",
                    "text": "Equilateral Triangle (Side=6cm)",
                    "image": {
                        "type": "svg",
                        "svg": svg_templates.svg_to_json_string(svg_templates.triangle((6, 6, 6), unit='cm')).strip('"'),
                        "alt": {"en": "Triangle with all sides 6 cm", "kn": "6 ಸೆಂ.ಮೀ ನ ಎಲ್ಲಾ ಬದಿಗಳಿರುವ ತ್ರಿಭುಜ"}
                    }
                }
            ],
            "answer": "optB",
            "reasoning": "Square perimeter = 16 cm. Rectangle perimeter = 20 cm (7+3+7+3). Triangle perimeter = 18 cm. Rectangle is largest."
        },
        "kn": {
            "question": "ಈ ಆಕಾರಗಳಲ್ಲಿ ಯಾವುದು ಅತಿ ದೊಡ್ಡ ಸುತ್ತಳತೆಯನ್ನು ಹೊಂದಿದೆ?",
            "options": [
                {
                    "id": "optA",
                    "text": "ಚೌಕ (ಬದಿ=4ಸೆಂ.ಮೀ)",
                    "image": {
                        "type": "svg",
                        "svg": svg_templates.svg_to_json_string(svg_templates.square(4, 'cm')).strip('"'),
                        "alt": {"en": "Square with side 4 cm", "kn": "4 ಸೆಂ.ಮೀ ಬದಿಯಿರುವ ಚೌಕ"}
                    }
                },
                {
                    "id": "optB",
                    "text": "ಆಯತ (7ಸೆಂ.ಮೀ × 3ಸೆಂ.ಮೀ)",
                    "image": {
                        "type": "svg",
                        "svg": svg_templates.svg_to_json_string(svg_templates.rectangle(7, 3, 'cm')).strip('"'),
                        "alt": {"en": "Rectangle with sides 7 cm and 3 cm", "kn": "7 ಸೆಂ.ಮೀ ಮತ್ತು 3 ಸೆಂ.ಮೀ ಬದಿಗಳ ಆಯತ"}
                    }
                },
                {
                    "id": "optC",
                    "text": "ಸಮಬಾಹು ತ್ರಿಭುಜ (ಬದಿ=6ಸೆಂ.ಮೀ)",
                    "image": {
                        "type": "svg",
                        "svg": svg_templates.svg_to_json_string(svg_templates.triangle((6, 6, 6), unit='cm')).strip('"'),
                        "alt": {"en": "Triangle with all sides 6 cm", "kn": "6 ಸೆಂ.ಮೀ ನ ಎಲ್ಲಾ ಬದಿಗಳಿರುವ ತ್ರಿಭುಜ"}
                    }
                }
            ],
            "answer": "optB",
            "reasoning": "ಚೌಕದ ಸುತ್ತಳತೆ = 16 ಸೆಂ.ಮೀ. ಆಯತದ ಸುತ್ತಳತೆ = 20 ಸೆಂ.ಮೀ. ತ್ರಿಭುಜದ ಸುತ್ತಳತೆ = 18 ಸೆಂ.ಮೀ. ಆದ್ದರಿಂದ ಆಯತವು ದೊಡ್ಡದಾಗಿದೆ."
        }
    }
    
    # Remove existing image questions to avoid duplicates if run multiple times
    questions = [q for q in questions if not q["id"].startswith("c6_math_pa_img_")]
    
    questions.extend([q1, q2, q3])
    
    with open(questions_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
        
    print(f"Added {len([q1, q2, q3])} test image questions to {questions_file}")

if __name__ == '__main__':
    main()
