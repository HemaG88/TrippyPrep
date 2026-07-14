from services.json_loader import JSONLoader
from services.quiz_engine import QuizEngine


questions = JSONLoader.load(
    "data/aptitude/01_foundation/number_system.json"
)

quiz = QuizEngine(questions)

print("=" * 50)
print("TrippyPrep Quiz Engine Test")
print("=" * 50)

while quiz.has_next():

    q = quiz.current_question()

    print(f"\nQuestion {quiz.current_number()}")
    print(q["question"])

    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")

    # Automatically choose the correct answer for testing
    answer = q["correct_option"]

    if quiz.check_answer(answer):
        print("✅ Correct")
    else:
        print("❌ Wrong")

    quiz.next_question()

print("\nQuiz Finished")
print(f"Final Score: {quiz.get_score()}/{quiz.total_questions()}")