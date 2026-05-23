# ============================================
#   AI Quiz Generator
#   Python with Generative AI Internship
#   Think Champ - May 2026
# ============================================

import random
import time

# Quiz Questions Database (AI / Python / General Knowledge)
QUESTIONS = [
    {
        "question": "What does AI stand for?",
        "options": ["A) Automated Input", "B) Artificial Intelligence", "C) Advanced Internet", "D) Applied Information"],
        "answer": "B",
        "explanation": "AI stands for Artificial Intelligence - machines that simulate human thinking."
    },
    {
        "question": "Which Python function prints output to the screen?",
        "options": ["A) input()", "B) display()", "C) print()", "D) show()"],
        "answer": "C",
        "explanation": "print() is used to display output in Python."
    },
    {
        "question": "What is a 'loop' in programming?",
        "options": ["A) A type of variable", "B) A repeating block of code", "C) A function name", "D) An error message"],
        "answer": "B",
        "explanation": "A loop repeats a block of code multiple times."
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A) Rectangle", "B) Integer", "C) Column", "D) Slide"],
        "answer": "B",
        "explanation": "Integer (int) is a Python data type for whole numbers."
    },
    {
        "question": "What does a chatbot use to understand questions?",
        "options": ["A) GPS", "B) Natural Language Processing", "C) Camera", "D) Keyboard shortcut"],
        "answer": "B",
        "explanation": "NLP (Natural Language Processing) helps AI understand human language."
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C",
        "explanation": "The 'def' keyword is used to define functions in Python."
    },
    {
        "question": "Which company created the ChatGPT AI?",
        "options": ["A) Google", "B) Microsoft", "C) OpenAI", "D) Apple"],
        "answer": "C",
        "explanation": "ChatGPT was created by OpenAI, founded in 2015."
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A) //", "B) /* */", "C) #", "D) --"],
        "answer": "C",
        "explanation": "The # symbol is used to write comments in Python."
    },
    {
        "question": "What is machine learning?",
        "options": ["A) Teaching machines to type", "B) Machines learning from data to make decisions", "C) Downloading software", "D) Writing machine code"],
        "answer": "B",
        "explanation": "Machine learning is when computers learn patterns from data without being explicitly programmed."
    },
    {
        "question": "Which of these stores a list of items in Python?",
        "options": ["A) String", "B) Boolean", "C) List", "D) Float"],
        "answer": "C",
        "explanation": "A List in Python stores multiple items in a single variable."
    }
]

def display_banner():
    print("\n" + "="*50)
    print("      🤖  AI QUIZ GENERATOR  🤖")
    print("   Python with Generative AI Internship")
    print("          Think Champ - 2026")
    print("="*50)

def get_player_name():
    print("\nWelcome to the AI Quiz Generator!")
    name = input("Please enter your name: ").strip()
    if not name:
        name = "Player"
    return name

def ask_question(question_data, question_number, total):
    print(f"\n{'─'*50}")
    print(f"Question {question_number} of {total}")
    print(f"{'─'*50}")
    print(f"\n❓ {question_data['question']}\n")
    
    for option in question_data['options']:
        print(f"   {option}")
    
    print()
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("⚠️  Please enter A, B, C, or D only.")

def check_answer(user_answer, question_data):
    correct = question_data['answer']
    if user_answer == correct:
        print("\n✅ CORRECT! Well done!")
        print(f"💡 {question_data['explanation']}")
        return True
    else:
        print(f"\n❌ Wrong! The correct answer was: {correct}")
        print(f"💡 {question_data['explanation']}")
        return False

def show_results(name, score, total, time_taken):
    percentage = (score / total) * 100
    print("\n" + "="*50)
    print("           📊 QUIZ RESULTS")
    print("="*50)
    print(f"\n  Player   : {name}")
    print(f"  Score    : {score} / {total}")
    print(f"  Accuracy : {percentage:.1f}%")
    print(f"  Time     : {time_taken:.1f} seconds")
    
    print("\n  Performance:")
    if percentage == 100:
        print("  🏆 PERFECT SCORE! You are a genius!")
    elif percentage >= 80:
        print("  🌟 Excellent! You know your stuff!")
    elif percentage >= 60:
        print("  👍 Good job! Keep learning!")
    elif percentage >= 40:
        print("  📚 Not bad! Study more and try again.")
    else:
        print("  💪 Keep practicing! You'll get better!")
    
    print("\n" + "="*50)

def run_quiz():
    display_banner()
    name = get_player_name()
    
    # Select random 5 questions from the database
    selected = random.sample(QUESTIONS, 5)
    score = 0
    total = len(selected)
    
    print(f"\nHello {name}! Get ready for {total} questions.")
    print("Topic: Python & Artificial Intelligence")
    input("\nPress ENTER to start the quiz... ")
    
    start_time = time.time()
    
    for i, question in enumerate(selected, 1):
        user_answer = ask_question(question, i, total)
        if check_answer(user_answer, question):
            score += 1
        time.sleep(1)
    
    end_time = time.time()
    time_taken = end_time - start_time
    
    show_results(name, score, total, time_taken)
    
    print("\nWould you like to play again?")
    again = input("Enter 'yes' to play again or any key to exit: ").strip().lower()
    if again == 'yes':
        run_quiz()
    else:
        print(f"\nThank you for playing, {name}! Goodbye! 👋\n")

# ─── Entry Point ───────────────────────────
if __name__ == "__main__":
    run_quiz()
