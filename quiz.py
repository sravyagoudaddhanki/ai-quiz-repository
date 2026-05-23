# ============================================
#   AI Quiz Generator
#   Think Champ Internship - Python with Gen AI
#   Project by: sravyagoudaddhanki
# ============================================

import random
import time
import os

QUESTIONS_FILE = "questions.txt"
SCORES_FILE = "scores.txt"

# ─── Load Questions from File ───────────────
def load_questions():
    questions = []
    try:
        with open(QUESTIONS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        questions.append({
                            "question": parts[0],
                            "answer": parts[1].lower(),
                            "explanation": parts[2]
                        })
    except FileNotFoundError:
        print(f"Error: {QUESTIONS_FILE} not found!")
    return questions

# ─── Save Score to File ──────────────────────
def save_score(name, score, total, time_taken):
    with open(SCORES_FILE, "a") as f:
        f.write(f"Name: {name} | Score: {score}/{total} | Time: {time_taken:.1f}s\n")
    print(f"\n✅ Score saved to {SCORES_FILE}")

# ─── Display Welcome Message ─────────────────
def welcome():
    print("=" * 45)
    print("     Welcome to AI Quiz Generator!")
    print("     Think Champ Internship Project")
    print("=" * 45)

# ─── Ask a Single Question ───────────────────
def ask_question(q_num, total, question_data):
    print(f"\nQuestion {q_num} of {total}:")
    print(question_data["question"])
    user_answer = input("Your Answer: ").strip().lower()
    return user_answer

# ─── Validate Answer ─────────────────────────
def validate_answer(user_answer, question_data):
    correct = question_data["answer"]
    if user_answer == correct:
        print("Correct Answer!")
        print(f"Explanation: {question_data['explanation']}")
        return True
    else:
        print(f"Wrong Answer! Correct answer is: {correct}")
        print(f"Explanation: {question_data['explanation']}")
        return False

# ─── Display Final Result ────────────────────
def display_result(name, score, total, time_taken):
    percentage = (score / total) * 100
    print("\n" + "=" * 45)
    print("           FINAL RESULT")
    print("=" * 45)
    print(f"Final Score: {score}/{total}")
    print(f"Percentage : {percentage:.1f}%")
    print(f"Time Taken : {time_taken:.1f} seconds")

    if percentage == 100:
        print("Performance: EXCELLENT! Perfect Score! 🏆")
    elif percentage >= 80:
        print("Performance: GREAT! Well done! 🌟")
    elif percentage >= 60:
        print("Performance: GOOD! Keep it up! 👍")
    elif percentage >= 40:
        print("Performance: AVERAGE! Study more! 📚")
    else:
        print("Performance: KEEP PRACTICING! 💪")
    print("=" * 45)

# ─── Main Quiz Function ──────────────────────
def run_quiz():
    welcome()

    name = input("\nEnter your name: ").strip()
    if not name:
        name = "Student"

    questions = load_questions()
    if not questions:
        print("No questions found! Please check questions.txt")
        return

    selected = random.sample(questions, min(5, len(questions)))
    total = len(selected)
    score = 0

    print(f"\nHello {name}! Get ready for {total} questions.")
    input("Press ENTER to start...")

    start_time = time.time()

    for i, question in enumerate(selected, 1):
        user_answer = ask_question(i, total, question)
        if validate_answer(user_answer, question):
            score += 1

    end_time = time.time()
    time_taken = end_time - start_time

    display_result(name, score, total, time_taken)
    save_score(name, score, total, time_taken)

    print("\nWould you like to play again? (yes/no)")
    again = input("Your choice: ").strip().lower()
    if again == "yes":
        run_quiz()
    else:
        print(f"\nThank you for playing, {name}! Goodbye! 👋")

# ─── Entry Point ────────────────────────────
if __name__ == "__main__":
    run_quiz()
