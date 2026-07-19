import re

def parse_quiz_text(quiz_text):
    """
    Converts Gemini's raw text output into a list of structured question dicts:
    [{ "question": ..., "options": {"A": ..., "B": ..., "C": ..., "D": ...},
       "correct": "B", "explanation": ... }, ...]
    Skips any block that doesn't match the expected format instead of crashing.
    """
    blocks = quiz_text.strip().split("---")
    parsed_questions = []

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        question_match = re.search(r"Question:\s*(.+)", block)
        option_a = re.search(r"A\)\s*(.+)", block)
        option_b = re.search(r"B\)\s*(.+)", block)
        option_c = re.search(r"C\)\s*(.+)", block)
        option_d = re.search(r"D\)\s*(.+)", block)
        correct_match = re.search(r"Correct Answer:\s*([A-D])", block)
        explanation_match = re.search(r"Explanation:\s*(.+)", block, re.DOTALL)

        if not all([question_match, option_a, option_b, option_c, option_d, correct_match]):
            continue  # skip malformed blocks instead of crashing the app

        parsed_questions.append({
            "question": question_match.group(1).strip(),
            "options": {
                "A": option_a.group(1).strip(),
                "B": option_b.group(1).strip(),
                "C": option_c.group(1).strip(),
                "D": option_d.group(1).strip(),
            },
            "correct": correct_match.group(1).strip(),
            "explanation": explanation_match.group(1).strip() if explanation_match else "No explanation provided.",
        })

    return parsed_questions