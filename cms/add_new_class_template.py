"""
add_new_class_template.py
=========================
REUSABLE TEMPLATE for adding a new class (e.g. Class 9, Class 10) to the
Bhagiratha Quiz app.

USAGE:
  1. Copy this file and rename it, e.g.: add_class_9_catalog.py
  2. Fill in all the TODO sections below.
  3. Run: python3 cms/add_class_9_catalog.py
  4. Run: python3 cms/verify_db.py   (must pass with zero errors)
  5. Run: npm run build              (must compile without errors)
  6. git add + git commit + git push

BILINGUAL SUPPORT RULES (read carefully):
  ─────────────────────────────────────────────────────────────────────────
  The menuTranslations.json file drives the Kannada language mode.
  Two different key formats are used:

  [A] CLASS and SUBJECT keys → plain Kannada STRING
      "class_9"           : "ತರಗತಿ 9 (NCERT)"
      "class_9/maths"     : "ಗಣಿತ"

  [B] CHAPTER keys → {en, kn} OBJECT
      "chapter_id"        : { "en": "English Name", "kn": "ಕನ್ನಡ ಹೆಸರು" }

  ⚠️  CRITICAL: If you omit the class/subject plain-string keys [A],
  the class and subjects will remain in English even when the user
  switches to Kannada. Always add ALL of:
      "class_X"
      "class_X/maths"
      "class_X/science"
      "class_X/english"
      "class_X/history"
      "class_X/kannada"
      (and any other subject IDs for that class)
  ─────────────────────────────────────────────────────────────────────────
"""

import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(BASE, 'src', 'data', 'catalog.json')
MENU_PATH    = os.path.join(BASE, 'src', 'data', 'menuTranslations.json')

# ═══════════════════════════════════════════════════════════════════════════
# TODO 1: Set the class ID and display names
# ═══════════════════════════════════════════════════════════════════════════
CLASS_ID   = "class_9"                  # e.g. "class_9"
CLASS_NAME = "Class 9 (NCERT)"          # English display name in catalog.json

# ═══════════════════════════════════════════════════════════════════════════
# TODO 2: Define subjects and their chapters
# Each chapter must have a unique "id" and an English "name".
# Use a class-prefixed format for English/History/Kannada chapters
# to avoid ID collisions across classes (e.g., "c9_eng_beehive").
# ═══════════════════════════════════════════════════════════════════════════
SUBJECTS = [
    {
        "id": "maths",
        "name": "Mathematics",
        "chapters": [
            # TODO: Fill with Class 9 maths chapters
            { "id": "number_systems",   "name": "Number Systems" },
            { "id": "polynomials",      "name": "Polynomials" },
            { "id": "coordinate_geometry", "name": "Coordinate Geometry" },
            { "id": "linear_equations_2var", "name": "Linear Equations in Two Variables" },
            { "id": "euclid_geometry",  "name": "Introduction to Euclid's Geometry" },
            { "id": "lines_angles",     "name": "Lines and Angles" },
            { "id": "triangles_c9",     "name": "Triangles" },
            { "id": "quadrilaterals_c9","name": "Quadrilaterals" },
            { "id": "circles_c9",       "name": "Circles" },
            { "id": "heron_formula",    "name": "Heron's Formula" },
            { "id": "surface_areas_volumes", "name": "Surface Areas and Volumes" },
            { "id": "statistics_c9",    "name": "Statistics" },
        ]
    },
    {
        "id": "science",
        "name": "Science",
        "chapters": [
            # TODO: Fill with Class 9 science chapters
            { "id": "matter_surroundings", "name": "Matter in Our Surroundings" },
            { "id": "pure_substance",   "name": "Is Matter Around Us Pure?" },
            { "id": "atoms_molecules",  "name": "Atoms and Molecules" },
            { "id": "structure_atom",   "name": "Structure of the Atom" },
            { "id": "cell_fundamental", "name": "The Fundamental Unit of Life" },
            { "id": "tissues",          "name": "Tissues" },
            { "id": "motion",           "name": "Motion" },
            { "id": "force_laws",       "name": "Force and Laws of Motion" },
            { "id": "gravitation",      "name": "Gravitation" },
            { "id": "work_energy",      "name": "Work and Energy" },
            { "id": "sound_c9",         "name": "Sound" },
            { "id": "natural_resources","name": "Natural Resources" },
        ]
    },
    {
        "id": "english",
        "name": "English (Beehive)",
        "chapters": [
            # TODO: Fill with Class 9 English chapters (prefix c9_eng_)
            { "id": "c9_eng_fun",       "name": "The Fun They Had" },
            { "id": "c9_eng_sound_music","name": "The Sound of Music" },
            { "id": "c9_eng_little_girl","name": "The Little Girl" },
            { "id": "c9_eng_truly_beautiful","name": "A Truly Beautiful Mind" },
            { "id": "c9_eng_snake",     "name": "The Snake and the Mirror" },
        ]
    },
    {
        "id": "history",
        "name": "History (India and the Contemporary World - I)",
        "chapters": [
            # TODO: Fill with Class 9 history chapters (prefix c9_his_)
            { "id": "c9_his_french_rev","name": "The French Revolution" },
            { "id": "c9_his_socialism", "name": "Socialism in Europe and the Russian Revolution" },
            { "id": "c9_his_nazism",    "name": "Nazism and the Rise of Hitler" },
            { "id": "c9_his_forests",   "name": "Forest Society and Colonialism" },
            { "id": "c9_his_pastoralists","name": "Pastoralists in the Modern World" },
        ]
    },
    {
        "id": "kannada",
        "name": "Kannada",
        "chapters": [
            # TODO: Fill with Class 9 Kannada chapters (prefix c9_kan_)
            { "id": "c9_kan_chapter1",  "name": "ಅಧ್ಯಾಯ 1" },
            { "id": "c9_kan_chapter2",  "name": "ಅಧ್ಯಾಯ 2" },
        ]
    },
]

# ═══════════════════════════════════════════════════════════════════════════
# TODO 3: Add Kannada translations for the class, subjects, and chapters
# ═══════════════════════════════════════════════════════════════════════════
TRANSLATIONS = {
    # ─────────────────────────────────────────────────────────────
    # [A] CLASS and SUBJECT top-level keys → plain Kannada strings
    #     These are MANDATORY for bilingual support.
    #     Key pattern: "class_X" and "class_X/subject_id"
    # ─────────────────────────────────────────────────────────────
    CLASS_ID:                   "ತರಗತಿ 9 (NCERT)",        # TODO: update Kannada class name
    f"{CLASS_ID}/maths":        "ಗಣಿತ",
    f"{CLASS_ID}/science":      "ವಿಜ್ಞಾನ",
    f"{CLASS_ID}/english":      "ಇಂಗ್ಲಿಷ್ (ಬೀಹೈವ್)",        # TODO: update if book name differs
    f"{CLASS_ID}/history":      "ಇತಿಹಾಸ (ಭಾರತ ಮತ್ತು ಸಮಕಾಲೀನ ಜಗತ್ತು - I)",  # TODO
    f"{CLASS_ID}/kannada":      "ಕನ್ನಡ",

    # ─────────────────────────────────────────────────────────────
    # [B] CHAPTER keys → {en, kn} objects
    #     Add one entry per chapter defined in SUBJECTS above.
    # ─────────────────────────────────────────────────────────────

    # Maths chapters
    "number_systems":       { "en": "Number Systems",                          "kn": "ಸಂಖ್ಯಾ ವ್ಯವಸ್ಥೆಗಳು" },
    "polynomials":          { "en": "Polynomials",                             "kn": "ಬಹುಪದೋಕ್ತಿಗಳು" },
    "coordinate_geometry":  { "en": "Coordinate Geometry",                     "kn": "ನಿರ್ದೇಶಾಂಕ ಜ್ಯಾಮಿತಿ" },
    "linear_equations_2var":{ "en": "Linear Equations in Two Variables",       "kn": "ಎರಡು ಚರಾಕ್ಷರಗಳ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳು" },
    "euclid_geometry":      { "en": "Introduction to Euclid's Geometry",       "kn": "ಯೂಕ್ಲಿಡ್ ಜ್ಯಾಮಿತಿ ಪರಿಚಯ" },
    "lines_angles":         { "en": "Lines and Angles",                        "kn": "ರೇಖೆಗಳು ಮತ್ತು ಕೋನಗಳು" },
    "triangles_c9":         { "en": "Triangles",                               "kn": "ತ್ರಿಭುಜಗಳು" },
    "quadrilaterals_c9":    { "en": "Quadrilaterals",                          "kn": "ಚತುರ್ಭುಜಗಳು" },
    "circles_c9":           { "en": "Circles",                                 "kn": "ವೃತ್ತಗಳು" },
    "heron_formula":        { "en": "Heron's Formula",                         "kn": "ಹೆರಾನ್ ಸೂತ್ರ" },
    "surface_areas_volumes":{ "en": "Surface Areas and Volumes",               "kn": "ಮೇಲ್ಮೈ ವಿಸ್ತೀರ್ಣ ಮತ್ತು ಘನಫಲ" },
    "statistics_c9":        { "en": "Statistics",                              "kn": "ಸಾಂಖ್ಯಿಕ" },

    # Science chapters
    "matter_surroundings":  { "en": "Matter in Our Surroundings",              "kn": "ನಮ್ಮ ಸುತ್ತಮುತ್ತಲಿನ ವಸ್ತು" },
    "pure_substance":       { "en": "Is Matter Around Us Pure?",               "kn": "ನಮ್ಮ ಸುತ್ತಮುತ್ತಲಿನ ವಸ್ತು ಶುದ್ಧವೇ?" },
    "atoms_molecules":      { "en": "Atoms and Molecules",                     "kn": "ಪರಮಾಣುಗಳು ಮತ್ತು ಅಣುಗಳು" },
    "structure_atom":       { "en": "Structure of the Atom",                   "kn": "ಪರಮಾಣುವಿನ ರಚನೆ" },
    "cell_fundamental":     { "en": "The Fundamental Unit of Life",            "kn": "ಜೀವನದ ಮೂಲ ಘಟಕ" },
    "tissues":              { "en": "Tissues",                                 "kn": "ಅಂಗಾಂಶಗಳು" },
    "motion":               { "en": "Motion",                                  "kn": "ಚಲನೆ" },
    "force_laws":           { "en": "Force and Laws of Motion",                "kn": "ಬಲ ಮತ್ತು ಚಲನೆಯ ನಿಯಮಗಳು" },
    "gravitation":          { "en": "Gravitation",                             "kn": "ಗುರುತ್ವಾಕರ್ಷಣೆ" },
    "work_energy":          { "en": "Work and Energy",                         "kn": "ಕಾರ್ಯ ಮತ್ತು ಶಕ್ತಿ" },
    "sound_c9":             { "en": "Sound",                                   "kn": "ಶಬ್ದ" },
    "natural_resources":    { "en": "Natural Resources",                       "kn": "ನೈಸರ್ಗಿಕ ಸಂಪನ್ಮೂಲಗಳು" },

    # English chapters
    "c9_eng_fun":           { "en": "The Fun They Had",                        "kn": "ಅವರು ಅನುಭವಿಸಿದ ಮೋಜು" },
    "c9_eng_sound_music":   { "en": "The Sound of Music",                      "kn": "ಸಂಗೀತದ ಧ್ವನಿ" },
    "c9_eng_little_girl":   { "en": "The Little Girl",                         "kn": "ಚಿಕ್ಕ ಹುಡುಗಿ" },
    "c9_eng_truly_beautiful":{ "en": "A Truly Beautiful Mind",                  "kn": "ನಿಜವಾಗಿಯೂ ಸುಂದರ ಮನಸ್ಸು" },
    "c9_eng_snake":         { "en": "The Snake and the Mirror",                "kn": "ಹಾವು ಮತ್ತು ಕನ್ನಡಿ" },

    # History chapters
    "c9_his_french_rev":    { "en": "The French Revolution",                   "kn": "ಫ್ರೆಂಚ್ ಕ್ರಾಂತಿ" },
    "c9_his_socialism":     { "en": "Socialism in Europe and the Russian Revolution", "kn": "ಯುರೋಪ್‌ನಲ್ಲಿ ಸಮಾಜವಾದ ಮತ್ತು ರಷ್ಯನ್ ಕ್ರಾಂತಿ" },
    "c9_his_nazism":        { "en": "Nazism and the Rise of Hitler",           "kn": "ನಾಝಿಸಂ ಮತ್ತು ಹಿಟ್ಲರನ ಉದಯ" },
    "c9_his_forests":       { "en": "Forest Society and Colonialism",          "kn": "ಅರಣ್ಯ ಸಮಾಜ ಮತ್ತು ವಸಾಹತುಶಾಹಿ" },
    "c9_his_pastoralists":  { "en": "Pastoralists in the Modern World",        "kn": "ಆಧುನಿಕ ಜಗತ್ತಿನಲ್ಲಿ ಪಶುಪಾಲಕರು" },

    # Kannada chapters — TODO: update with real chapter names
    "c9_kan_chapter1":      { "en": "Chapter 1 (Kannada)",                     "kn": "ಅಧ್ಯಾಯ 1" },
    "c9_kan_chapter2":      { "en": "Chapter 2 (Kannada)",                     "kn": "ಅಧ್ಯಾಯ 2" },
}


# ═══════════════════════════════════════════════════════════════════════════
# Core logic — do NOT edit below this line
# ═══════════════════════════════════════════════════════════════════════════

def update_catalog():
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    existing = next((c for c in catalog['classes'] if c['id'] == CLASS_ID), None)
    if existing:
        print(f"⚠️  {CLASS_ID} already exists in catalog — updating subjects.")
        existing['subjects'] = SUBJECTS
    else:
        catalog['classes'].append({
            "id": CLASS_ID,
            "name": CLASS_NAME,
            "subjects": SUBJECTS,
        })
        print(f"✅  Added {CLASS_ID} to catalog.")

    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print("   catalog.json saved.")


def update_menu():
    with open(MENU_PATH, 'r', encoding='utf-8') as f:
        menu = json.load(f)

    added, updated, skipped = [], [], []
    for key, val in TRANSLATIONS.items():
        if key not in menu:
            menu[key] = val
            added.append(key)
        elif menu[key] != val:
            menu[key] = val
            updated.append(key)
        else:
            skipped.append(key)

    with open(MENU_PATH, 'w', encoding='utf-8') as f:
        json.dump(menu, f, indent=2, ensure_ascii=False)

    print(f"\n✅  menuTranslations.json updated:")
    print(f"   Added   : {len(added)} keys")
    print(f"   Updated : {len(updated)} keys")
    print(f"   Skipped : {len(skipped)} keys (already correct)")


def verify_bilingual():
    """Sanity check: confirm all class+subject keys exist as plain strings."""
    with open(MENU_PATH, 'r', encoding='utf-8') as f:
        menu = json.load(f)

    required_string_keys = [CLASS_ID] + [f"{CLASS_ID}/{sub['id']}" for sub in SUBJECTS]
    errors = []
    for key in required_string_keys:
        val = menu.get(key)
        if val is None:
            errors.append(f"  ❌ MISSING: '{key}'")
        elif not isinstance(val, str):
            errors.append(f"  ❌ WRONG FORMAT: '{key}' should be a plain string, got {type(val).__name__}")
        else:
            print(f"  ✅ {key}: {val}")

    if errors:
        print("\n⚠️  BILINGUAL ERRORS FOUND — Kannada mode will be broken for:")
        for e in errors:
            print(e)
        raise SystemExit(1)
    else:
        print(f"\n✅  All {len(required_string_keys)} class/subject keys are correct plain strings.")


if __name__ == "__main__":
    print(f"=== Setting up {CLASS_ID} ===\n")
    update_catalog()
    print()
    update_menu()
    print()
    print("=== Verifying bilingual support ===")
    verify_bilingual()
    print(f"\n🎉  Done! Now run:")
    print(f"    python3 cms/verify_db.py")
    print(f"    npm run build")
    print(f"")
    print(f"    Then to push to main AND deploy to GitHub Pages in one step:")
    print(f"    npm run publish")
    print(f"")
    print(f"    ⚠️  NEVER use plain 'git push' alone — it does NOT update GitHub Pages!")
    print(f"    Always use 'npm run publish' as the final step.")
