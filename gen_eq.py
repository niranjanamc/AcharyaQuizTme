import json

questions = []
q = 1

def add_single(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_eq_{q:03d}", "type": "single", "difficulty": diff,
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_multiple(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_eq_{q:03d}", "type": "multiple", "difficulty": diff,
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_match(diff, en_q, kn_q, en_pairs, kn_pairs, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_eq_{q:03d}", "type": "match", "difficulty": diff,
        "en": {"question": en_q, "pairs": en_pairs, "reasoning": en_reas},
        "kn": {"question": kn_q, "pairs": kn_pairs, "reasoning": kn_reas}
    })
    q += 1

def add_img_s(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_eq_{q:03d}", "type": "image_single", "difficulty": diff,
        "image": {"type": "svg", "svg": svg.strip(), "alt": {"en": en_alt, "kn": kn_alt}},
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_img_m(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_eq_{q:03d}", "type": "image_multiple", "difficulty": diff,
        "image": {"type": "svg", "svg": svg.strip(), "alt": {"en": en_alt, "kn": kn_alt}},
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

# Easy (10)
add_single(1, "Solve for x: x + 5 = 12", "x ನ ಬೆಲೆಯನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ: x + 5 = 12", ["7", "17", "6", "8"], ["7", "17", "6", "8"], "7", "7", "Subtract 5 from both sides: x = 12 - 5 = 7.", "ಎರಡೂ ಕಡೆಯಿಂದ 5 ನ್ನು ಕಳೆಯಿರಿ: x = 12 - 5 = 7.")
add_single(1, "Write the equation for: 'The sum of a number y and 4 is 9'.", "'y ಮತ್ತು 4 ರ ಮೊತ್ತ 9' ಎಂಬುದಕ್ಕೆ ಸಮೀಕರಣವನ್ನು ಬರೆಯಿರಿ.", ["y - 4 = 9", "y + 4 = 9", "4y = 9", "y / 4 = 9"], ["y - 4 = 9", "y + 4 = 9", "4y = 9", "y / 4 = 9"], "y + 4 = 9", "y + 4 = 9", "Sum means addition, so y + 4 = 9.", "ಮೊತ್ತ ಎಂದರೆ ಸಂಕಲನ, ಆದ್ದರಿಂದ y + 4 = 9.")
add_single(1, "Solve the equation: 3n = 21", "ಸಮೀಕರಣವನ್ನು ಬಿಡಿಸಿ: 3n = 21", ["n = 18", "n = 7", "n = 63", "n = 6"], ["n = 18", "n = 7", "n = 63", "n = 6"], "n = 7", "n = 7", "Divide both sides by 3: n = 21 / 3 = 7.", "ಎರಡೂ ಕಡೆ 3 ರಿಂದ ಭಾಗಿಸಿ: n = 21 / 3 = 7.")
add_single(1, "What is the value of p if p/2 = 8?", "p/2 = 8 ಆದರೆ, p ನ ಬೆಲೆ ಎಷ್ಟು?", ["4", "10", "16", "6"], ["4", "10", "16", "6"], "16", "16", "Multiply both sides by 2: p = 8 × 2 = 16.", "ಎರಡೂ ಕಡೆ 2 ರಿಂದ ಗುಣಿಸಿ: p = 8 × 2 = 16.")
add_single(1, "Which of the following is a simple equation?", "ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಳ ಸಮೀಕರಣವಾಗಿದೆ?", ["2x + 3", "x - 5 > 0", "4y = 12", "5 + 2 = 7"], ["2x + 3", "x - 5 > 0", "4y = 12", "5 + 2 = 7"], "4y = 12", "4y = 12", "An equation must have an equal sign (=) and a variable. '4y = 12' satisfies this.", "ಒಂದು ಸಮೀಕರಣವು ಸಮ ಚಿಹ್ನೆ (=) ಮತ್ತು ಚರಾಕ್ಷರವನ್ನು ಹೊಂದಿರಬೇಕು. '4y = 12' ಇದನ್ನು ಪೂರೈಸುತ್ತದೆ.")
add_single(1, "Solve for x: x - 7 = -2", "x ನ ಬೆಲೆಯನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ: x - 7 = -2", ["5", "-5", "9", "-9"], ["5", "-5", "9", "-9"], "5", "5", "Add 7 to both sides: x = -2 + 7 = 5.", "ಎರಡೂ ಕಡೆ 7 ನ್ನು ಸೇರಿಸಿ: x = -2 + 7 = 5.")

add_img_s(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <line x1="50" y1="150" x2="250" y2="150" stroke="#1F2937" stroke-width="4"/>
  <polygon points="150,150 140,170 160,170" fill="#1F2937"/>
  <rect x="70" y="110" width="40" height="40" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="90" y="135" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">x</text>
  <circle cx="120" cy="130" r="10" fill="#059669"/>
  <text x="120" y="135" fill="white" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">3</text>
  <circle cx="200" cy="130" r="10" fill="#059669"/>
  <text x="200" y="135" fill="white" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">10</text>
</svg>""", "A balanced scale. On the left: a box labeled 'x' and a weight of 3. On the right: a weight of 10.", "ಸಮತೋಲಿತ ತಕ್ಕಡಿ. ಎಡಭಾಗದಲ್ಲಿ: 'x' ಎಂಬ ಬಾಕ್ಸ್ ಮತ್ತು 3 ರ ತೂಕ. ಬಲಭಾಗದಲ್ಲಿ: 10 ರ ತೂಕ.", "The scale is perfectly balanced. What is the value of x?", "ತಕ್ಕಡಿ ಸಂಪೂರ್ಣವಾಗಿ ಸಮತೋಲನದಲ್ಲಿದೆ. x ನ ಬೆಲೆ ಎಷ್ಟು?", ["13", "7", "30", "10"], ["13", "7", "30", "10"], "7", "7", "The equation is x + 3 = 10, so x = 7.", "ಸಮೀಕರಣ x + 3 = 10, ಆದ್ದರಿಂದ x = 7.")

add_img_s(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150">
  <rect x="50" y="50" width="200" height="40" fill="none" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="50" x2="150" y2="90" stroke="#2563EB" stroke-width="2"/>
  <text x="100" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">x</text>
  <text x="200" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">x</text>
  <line x1="50" y1="100" x2="250" y2="100" stroke="#EA580C" stroke-width="2"/>
  <path d="M 50,100 L 50,110" fill="none" stroke="#EA580C" stroke-width="2"/>
  <path d="M 250,100 L 250,110" fill="none" stroke="#EA580C" stroke-width="2"/>
  <text x="150" y="125" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">18</text>
</svg>""", "A bar showing two equal parts labeled x and x. The total length is 18.", "x ಮತ್ತು x ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ ಎರಡು ಸಮಾನ ಭಾಗಗಳನ್ನು ತೋರಿಸುವ ಪಟ್ಟಿ. ಒಟ್ಟು ಉದ್ದ 18.", "What is the value of x?", "x ನ ಬೆಲೆ ಎಷ್ಟು?", ["8", "9", "18", "36"], ["8", "9", "18", "36"], "9", "9", "From the figure, x + x = 18 => 2x = 18 => x = 9.", "ಚಿತ್ರದ ಪ್ರಕಾರ, x + x = 18 => 2x = 18 => x = 9.")

add_multiple(1, "Which of the equations have x = 4 as a solution?", "ಯಾವ ಸಮೀಕರಣಗಳು x = 4 ನ್ನು ಪರಿಹಾರವಾಗಿ ಹೊಂದಿವೆ?", ["x + 2 = 6", "2x = 8", "x - 4 = 1", "3x = 12"], ["x + 2 = 6", "2x = 8", "x - 4 = 1", "3x = 12"], ["x + 2 = 6", "2x = 8", "3x = 12"], ["x + 2 = 6", "2x = 8", "3x = 12"], "Substitute x = 4. 4+2=6 (True), 2(4)=8 (True), 4-4=0!=1 (False), 3(4)=12 (True).", "x = 4 ನ್ನು ಆದೇಶಿಸಿ. 4+2=6 (ಸರಿ), 2(4)=8 (ಸರಿ), 4-4=0!=1 (ತಪ್ಪು), 3(4)=12 (ಸರಿ).")

add_match(1, "Match the statement with its algebraic equation:", "ಹೇಳಿಕೆಯನ್ನು ಅದರ ಬೀಜಗಣಿತ ಸಮೀಕರಣದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Twice a number is 10", "right": "2x = 10"}, {"left": "A number increased by 2 is 10", "right": "x + 2 = 10"}, {"left": "A number decreased by 2 is 10", "right": "x - 2 = 10"}, {"left": "Half of a number is 10", "right": "x / 2 = 10"}], [{"left": "ಒಂದು ಸಂಖ್ಯೆಯ ಎರಡರಷ್ಟು 10", "right": "2x = 10"}, {"left": "ಒಂದು ಸಂಖ್ಯೆಯನ್ನು 2 ಹೆಚ್ಚಿಸಿದಾಗ 10", "right": "x + 2 = 10"}, {"left": "ಒಂದು ಸಂಖ್ಯೆಯನ್ನು 2 ರಷ್ಟು ಕಡಿಮೆ ಮಾಡಿದಾಗ 10", "right": "x - 2 = 10"}, {"left": "ಒಂದು ಸಂಖ್ಯೆಯ ಅರ್ಧ ಭಾಗ 10", "right": "x / 2 = 10"}], "Translating English phrases into mathematical operations.", "ಇಂಗ್ಲಿಷ್ ಪದಗುಚ್ಛಗಳನ್ನು ಗಣಿತದ ಲೆಕ್ಕಾಚಾರಗಳಿಗೆ ಅನುವಾದಿಸುವುದು.")


# Medium (10)
add_single(2, "Solve the equation: 5p + 2 = 17", "ಸಮೀಕರಣವನ್ನು ಬಿಡಿಸಿ: 5p + 2 = 17", ["3", "15", "5", "7"], ["3", "15", "5", "7"], "3", "3", "5p = 17 - 2 => 5p = 15 => p = 3.", "5p = 17 - 2 => 5p = 15 => p = 3.")
add_single(2, "Raju's father's age is 5 years more than three times Raju's age. If his father is 44 years old, how old is Raju?", "ರಾಜುವಿನ ತಂದೆಯ ವಯಸ್ಸು ರಾಜುವಿನ ವಯಸ್ಸಿನ ಮೂರರಷ್ಟಕ್ಕಿಂತ 5 ವರ್ಷ ಹೆಚ್ಚು. ಅವನ ತಂದೆಗೆ 44 ವರ್ಷಗಳಾಗಿದ್ದರೆ, ರಾಜುವಿನ ವಯಸ್ಸೆಷ್ಟು?", ["11", "12", "13", "15"], ["11", "12", "13", "15"], "13", "13", "Let Raju's age be y. 3y + 5 = 44 => 3y = 39 => y = 13.", "ರಾಜುವಿನ ವಯಸ್ಸು y ಆಗಿರಲಿ. 3y + 5 = 44 => 3y = 39 => y = 13.")
add_single(2, "Solve: 4(m + 3) = 18", "ಬಿಡಿಸಿ: 4(m + 3) = 18", ["1.5", "2.5", "6", "-1.5"], ["1.5", "2.5", "6", "-1.5"], "1.5", "1.5", "m + 3 = 18 / 4 = 4.5. Therefore, m = 4.5 - 3 = 1.5.", "m + 3 = 18 / 4 = 4.5. ಆದ್ದರಿಂದ, m = 4.5 - 3 = 1.5.")
add_single(2, "Find x: x/3 + 5/2 = -3/2", "x ನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ: x/3 + 5/2 = -3/2", ["-12", "12", "-4", "4"], ["-12", "12", "-4", "4"], "-12", "-12", "x/3 = -3/2 - 5/2 = -8/2 = -4. x = -4 × 3 = -12.", "x/3 = -3/2 - 5/2 = -8/2 = -4. x = -4 × 3 = -12.")
add_single(2, "If 7x - 4 = 3x + 16, what is the value of x?", "7x - 4 = 3x + 16 ಆದರೆ, x ನ ಬೆಲೆ ಎಷ್ಟು?", ["4", "5", "6", "10"], ["4", "5", "6", "10"], "5", "5", "7x - 3x = 16 + 4 => 4x = 20 => x = 5.", "7x - 3x = 16 + 4 => 4x = 20 => x = 5.")

add_img_s(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <polygon points="150,30 250,150 50,150" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="80" y="90" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" transform="rotate(-50, 80, 90)">2x</text>
  <text x="220" y="90" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" transform="rotate(50, 220, 90)">2x</text>
  <text x="150" y="170" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">10</text>
</svg>""", "An isosceles triangle with equal sides labeled 2x and the base labeled 10.", "2x ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ ಸಮಾನ ಬಾಹುಗಳು ಮತ್ತು 10 ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ ಪಾದವನ್ನು ಹೊಂದಿರುವ ಸಮದ್ವಿಬಾಹು ತ್ರಿಕೋನ.", "If the perimeter of the triangle is 34 cm, find the value of x.", "ತ್ರಿಕೋನದ ಸುತ್ತಳತೆ 34 ಸೆಂ.ಮೀ ಆಗಿದ್ದರೆ, x ನ ಬೆಲೆಯನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["5", "6", "8", "12"], ["5", "6", "8", "12"], "6", "6", "Perimeter = 2x + 2x + 10 = 34 => 4x = 24 => x = 6.", "ಸುತ್ತಳತೆ = 2x + 2x + 10 = 34 => 4x = 24 => x = 6.")

add_img_s(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="50" width="200" height="100" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="150" y="40" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">3y - 2</text>
  <text x="270" y="105" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">y</text>
</svg>""", "A rectangle with length labeled 3y - 2 and width labeled y.", "3y - 2 ಉದ್ದ ಮತ್ತು y ಅಗಲ ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ ಆಯತ.", "If the perimeter is 36, what is the value of y?", "ಸುತ್ತಳತೆ 36 ಆಗಿದ್ದರೆ, y ನ ಮೌಲ್ಯ ಎಷ್ಟು?", ["5", "6", "7", "4"], ["5", "6", "7", "4"], "5", "5", "Perimeter = 2(l + w) = 2(3y - 2 + y) = 2(4y - 2) = 8y - 4. So 8y - 4 = 36 => 8y = 40 => y = 5.", "ಸುತ್ತಳತೆ = 2(3y - 2 + y) = 2(4y - 2) = 8y - 4. 8y - 4 = 36 => 8y = 40 => y = 5.")

add_img_m(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150">
  <line x1="50" y1="100" x2="250" y2="100" stroke="#1F2937" stroke-width="4"/>
  <polygon points="150,100 140,120 160,120" fill="#1F2937"/>
  <rect x="70" y="60" width="30" height="40" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="85" y="85" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">y</text>
  <circle cx="110" cy="80" r="10" fill="#059669"/>
  <text x="110" y="85" fill="white" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">5</text>
  <circle cx="200" cy="80" r="10" fill="#059669"/>
  <text x="200" y="85" fill="white" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">12</text>
</svg>""", "A balance scale: Left has 'y' box and weight 5. Right has weight 12. Left is lower than right.", "ಸಮತೋಲನವಿಲ್ಲದ ತಕ್ಕಡಿ: ಎಡಭಾಗದಲ್ಲಿ 'y' ಬಾಕ್ಸ್ ಮತ್ತು 5 ತೂಕವಿದೆ. ಬಲಭಾಗದಲ್ಲಿ 12 ತೂಕವಿದೆ. ಎಡಭಾಗವು ಬಲಭಾಗಕ್ಕಿಂತ ಕೆಳಗಿದೆ.", "The left side of the scale is heavier than the right side. Which inequalities describe this situation?", "ತಕ್ಕಡಿಯ ಎಡಭಾಗವು ಬಲಭಾಗಕ್ಕಿಂತ ಭಾರವಾಗಿರುತ್ತದೆ. ಯಾವ ಅಸಮಾನತೆಗಳು ಈ ಪರಿಸ್ಥಿತಿಯನ್ನು ವಿವರಿಸುತ್ತವೆ?", ["y + 5 > 12", "y > 7", "y + 5 < 12", "y < 7"], ["y + 5 > 12", "y > 7", "y + 5 < 12", "y < 7"], ["y + 5 > 12", "y > 7"], ["y + 5 > 12", "y > 7"], "Since the left side is heavier, its weight is greater: y + 5 > 12. Solving gives y > 7.", "ಎಡಭಾಗವು ಭಾರವಾಗಿರುವುದರಿಂದ, ಅದರ ತೂಕವು ಹೆಚ್ಚಾಗಿರುತ್ತದೆ: y + 5 > 12. ಇದನ್ನು ಬಿಡಿಸಿದರೆ y > 7 ಬರುತ್ತದೆ.")

add_multiple(2, "Which equations have negative solutions?", "ಯಾವ ಸಮೀಕರಣಗಳು ಋಣಾತ್ಮಕ ಪರಿಹಾರಗಳನ್ನು ಹೊಂದಿವೆ?", ["x + 8 = 5", "3x = -15", "x - 2 = 4", "-2x = 10"], ["x + 8 = 5", "3x = -15", "x - 2 = 4", "-2x = 10"], ["x + 8 = 5", "3x = -15", "-2x = 10"], ["x + 8 = 5", "3x = -15", "-2x = 10"], "x+8=5 => x=-3. 3x=-15 => x=-5. x-2=4 => x=6. -2x=10 => x=-5.", "x+8=5 => x=-3. 3x=-15 => x=-5. -2x=10 => x=-5.")

add_match(2, "Match the equation to its solution:", "ಸಮೀಕರಣವನ್ನು ಅದರ ಪರಿಹಾರದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "2x + 1 = 9", "right": "x = 4"}, {"left": "3x - 1 = 8", "right": "x = 3"}, {"left": "4x + 2 = 10", "right": "x = 2"}, {"left": "5x - 3 = 2", "right": "x = 1"}], [{"left": "2x + 1 = 9", "right": "x = 4"}, {"left": "3x - 1 = 8", "right": "x = 3"}, {"left": "4x + 2 = 10", "right": "x = 2"}, {"left": "5x - 3 = 2", "right": "x = 1"}], "Solve each simple equation step-by-step.", "ಪ್ರತಿ ಸರಳ ಸಮೀಕರಣವನ್ನು ಹಂತ-ಹಂತವಾಗಿ ಬಿಡಿಸಿ.")


# Hard (10)
add_single(3, "Solve: 16 = 4 + 3(t + 2)", "ಬಿಡಿಸಿ: 16 = 4 + 3(t + 2)", ["2", "4", "0", "1"], ["2", "4", "0", "1"], "2", "2", "16 - 4 = 12 => 3(t + 2) = 12 => t + 2 = 4 => t = 2.", "16 - 4 = 12 => 3(t + 2) = 12 => t + 2 = 4 => t = 2.")
add_single(3, "The sum of three consecutive integers is 45. Find the smallest integer.", "ಮೂರು ಅನುಕ್ರಮ ಪೂರ್ಣಾಂಕಗಳ ಮೊತ್ತವು 45 ಆಗಿದೆ. ಅತ್ಯಂತ ಚಿಕ್ಕ ಪೂರ್ಣಾಂಕವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["13", "14", "15", "16"], ["13", "14", "15", "16"], "14", "14", "Let integers be x, x+1, x+2. 3x + 3 = 45 => 3x = 42 => x = 14.", "ಪೂರ್ಣಾಂಕಗಳು x, x+1, x+2 ಆಗಿರಲಿ. 3x + 3 = 45 => 3x = 42 => x = 14.")
add_single(3, "In an isosceles triangle, the base angles are equal. The vertex angle is 40°. What are the base angles of the triangle?", "ಸಮದ್ವಿಬಾಹು ತ್ರಿಕೋನದಲ್ಲಿ, ಪಾದದ ಕೋನಗಳು ಸಮಾನವಾಗಿರುತ್ತವೆ. ಶೃಂಗದ ಕೋನ 40°. ತ್ರಿಕೋನದ ಪಾದದ ಕೋನಗಳು ಯಾವುವು?", ["70°", "60°", "80°", "50°"], ["70°", "60°", "80°", "50°"], "70°", "70°", "Let base angle be x. x + x + 40 = 180 => 2x = 140 => x = 70°.", "ಪಾದದ ಕೋನ x ಆಗಿರಲಿ. x + x + 40 = 180 => 2x = 140 => x = 70°.")
add_single(3, "I am a number. Tell my identity! Take me seven times over, and add a fifty! To reach a triple century, you still need forty! Who am I?", "ನಾನೊಂದು ಸಂಖ್ಯೆ, ನನ್ನ ಗುರುತೇನು ಹೇಳಿ! ನನ್ನನ್ನು ಏಳು ಬಾರಿ ತೆಗೆದುಕೊಳ್ಳಿ, ಮತ್ತು 50 ಅನ್ನು ಸೇರಿಸಿ! 300 ಅನ್ನು ತಲುಪಲು, ನಿಮಗೆ ಇನ್ನೂ 40 ಬೇಕು! ನಾನು ಯಾರು?", ["30", "40", "50", "20"], ["30", "40", "50", "20"], "30", "30", "7x + 50 + 40 = 300 => 7x + 90 = 300 => 7x = 210 => x = 30.", "7x + 50 + 40 = 300 => 7x + 90 = 300 => 7x = 210 => x = 30.")

add_img_s(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="50" width="200" height="100" fill="none" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="50" x2="150" y2="150" stroke="#EA580C" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="100" y="105" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">2x - 1</text>
  <text x="200" y="105" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">x + 5</text>
</svg>""", "A rectangle divided into two parts. The areas are labeled 2x - 1 and x + 5.", "ಎರಡು ಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾದ ಆಯತ. ವಿಸ್ತೀರ್ಣಗಳನ್ನು 2x - 1 ಮತ್ತು x + 5 ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾಗಿದೆ.", "If the two shaded regions have exactly equal areas, what is the value of x?", "ಎರಡು ಛಾಯೆಗೊಳಿಸಿದ ಪ್ರದೇಶಗಳು ಒಂದೇ ವಿಸ್ತೀರ್ಣವನ್ನು ಹೊಂದಿದ್ದರೆ, x ನ ಬೆಲೆ ಎಷ್ಟು?", ["4", "5", "6", "7"], ["4", "5", "6", "7"], "6", "6", "Equate the areas: 2x - 1 = x + 5. Subtract x: x - 1 = 5. Add 1: x = 6.", "ವಿಸ್ತೀರ್ಣಗಳನ್ನು ಸಮೀಕರಿಸಿ: 2x - 1 = x + 5. x ಕಳೆಯಿರಿ: x - 1 = 5. 1 ಸೇರಿಸಿ: x = 6.")

add_img_m(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <path d="M 50,150 L 150,50 L 250,150 Z" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="90" y="100" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">2a</text>
  <text x="210" y="100" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">3b - 1</text>
  <text x="150" y="170" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">11</text>
</svg>""", "An equilateral triangle with sides 2a, 3b-1, and 11.", "2a, 3b-1, ಮತ್ತು 11 ಬಾಹುಗಳಿರುವ ಸಮಬಾಹು ತ್ರಿಕೋನ.", "If the triangle shown is an equilateral triangle, which of the following statements are true?", "ತೋರಿಸಿರುವ ತ್ರಿಕೋನವು ಸಮಬಾಹು ತ್ರಿಕೋನವಾಗಿದ್ದರೆ, ಕೆಳಗಿನ ಹೇಳಿಕೆಗಳಲ್ಲಿ ಯಾವುದು ಸರಿ?", ["a = 5.5", "b = 4", "a + b = 9.5", "Perimeter = 33"], ["a = 5.5", "b = 4", "a + b = 9.5", "ಸುತ್ತಳತೆ = 33"], ["a = 5.5", "b = 4", "a + b = 9.5", "Perimeter = 33"], ["a = 5.5", "b = 4", "a + b = 9.5", "ಸುತ್ತಳತೆ = 33"], "All sides equal 11. 2a = 11 => a = 5.5. 3b - 1 = 11 => 3b = 12 => b = 4. a+b = 9.5. Perimeter = 11*3 = 33.", "ಎಲ್ಲಾ ಬಾಹುಗಳು 11 ಕ್ಕೆ ಸಮ. 2a = 11 => a = 5.5. 3b - 1 = 11 => b = 4. a+b = 9.5. ಸುತ್ತಳತೆ = 33.")

add_multiple(3, "Which of these equations require more than one step to solve?", "ಈ ಕೆಳಗಿನ ಯಾವ ಸಮೀಕರಣಗಳನ್ನು ಬಿಡಿಸಲು ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಹಂತಗಳ ಅಗತ್ಯವಿದೆ?", ["2x + 1 = 9", "x - 5 = 10", "3(x - 2) = 15", "x/4 = 8"], ["2x + 1 = 9", "x - 5 = 10", "3(x - 2) = 15", "x/4 = 8"], ["2x + 1 = 9", "3(x - 2) = 15"], ["2x + 1 = 9", "3(x - 2) = 15"], "2x+1=9 requires subtraction then division. 3(x-2)=15 requires expansion/division then addition. The others are one-step.", "2x+1=9 ಗೆ ವ್ಯವಕಲನ ಮತ್ತು ನಂತರ ಭಾಗಾಕಾರ ಬೇಕು. 3(x-2)=15 ಕ್ಕೆ ಗುಣಾಕಾರ/ಭಾಗಾಕಾರ ಮತ್ತು ಸಂಕಲನ ಬೇಕು.")

add_match(3, "Match the equation to its root:", "ಸಮೀಕರಣವನ್ನು ಅದರ ಮೂಲದೊಂದಿಗೆ (root) ಹೊಂದಿಸಿ:", [{"left": "2(x + 3) = 10", "right": "2"}, {"left": "3(x - 1) = 12", "right": "5"}, {"left": "4x - 5 = 7", "right": "3"}, {"left": "x/2 + 3 = 7", "right": "8"}], [{"left": "2(x + 3) = 10", "right": "2"}, {"left": "3(x - 1) = 12", "right": "5"}, {"left": "4x - 5 = 7", "right": "3"}, {"left": "x/2 + 3 = 7", "right": "8"}], "Solve each two-step equation.", "ಪ್ರತಿ ಎರಡು ಹಂತದ ಸಮೀಕರಣವನ್ನು ಬಿಡಿಸಿ.")

add_match(3, "Match the word problem to the equation used to solve it:", "ಪದ ಸಮಸ್ಯೆಯನ್ನು ಬಿಡಿಸಲು ಬಳಸುವ ಸಮೀಕರಣದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Sum of a number and its double is 30", "right": "x + 2x = 30"}, {"left": "Number divided by 3, then 2 added gives 10", "right": "x/3 + 2 = 10"}, {"left": "5 less than three times a number is 25", "right": "3x - 5 = 25"}, {"left": "Twice the sum of a number and 4 is 20", "right": "2(x + 4) = 20"}], [{"left": "ಒಂದು ಸಂಖ್ಯೆ ಮತ್ತು ಅದರ ಎರಡರಷ್ಟರ ಮೊತ್ತ 30", "right": "x + 2x = 30"}, {"left": "ಸಂಖ್ಯೆಯನ್ನು 3 ರಿಂದ ಭಾಗಿಸಿ, ನಂತರ 2 ಸೇರಿಸಿದರೆ 10 ಸಿಗುತ್ತದೆ", "right": "x/3 + 2 = 10"}, {"left": "ಒಂದು ಸಂಖ್ಯೆಯ 3 ರಷ್ಟಕ್ಕಿಂತ 5 ಕಡಿಮೆ ಎಂದರೆ 25", "right": "3x - 5 = 25"}, {"left": "ಒಂದು ಸಂಖ್ಯೆ ಮತ್ತು 4 ರ ಮೊತ್ತದ ಎರಡರಷ್ಟು 20", "right": "2(x + 4) = 20"}], "Translating complex word problems into equations.", "ಸಂಕೀರ್ಣ ಪದ ಸಮಸ್ಯೆಗಳನ್ನು ಸಮೀಕರಣಗಳಾಗಿ ಅನುವಾದಿಸುವುದು.")

add_match(3, "Match the transformation applied to an equation (e.g. 2x = 8) to the result:", "ಸಮೀಕರಣಕ್ಕೆ (ಉದಾ. 2x = 8) ಅನ್ವಯಿಸಲಾದ ಬದಲಾವಣೆಯನ್ನು ಅದರ ಫಲಿತಾಂಶದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Add 3 to both sides", "right": "2x + 3 = 11"}, {"left": "Multiply both sides by 3", "right": "6x = 24"}, {"left": "Divide both sides by 2", "right": "x = 4"}, {"left": "Subtract x from both sides", "right": "x = 8 - x"}], [{"left": "ಎರಡೂ ಕಡೆಗೆ 3 ಸೇರಿಸಿ", "right": "2x + 3 = 11"}, {"left": "ಎರಡೂ ಕಡೆ 3 ರಿಂದ ಗುಣಿಸಿ", "right": "6x = 24"}, {"left": "ಎರಡೂ ಕಡೆ 2 ರಿಂದ ಭಾಗಿಸಿ", "right": "x = 4"}, {"left": "ಎರಡೂ ಕಡೆಯಿಂದ x ನ್ನು ಕಳೆಯಿರಿ", "right": "x = 8 - x"}], "Balancing an equation by performing the same operation on both sides.", "ಎರಡೂ ಕಡೆಗಳಲ್ಲಿ ಒಂದೇ ಕಾರ್ಯಾಚರಣೆಯನ್ನು ಮಾಡುವ ಮೂಲಕ ಸಮೀಕರಣವನ್ನು ಸಮತೋಲನಗೊಳಿಸುವುದು.")


with open('/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/simple_equations.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
