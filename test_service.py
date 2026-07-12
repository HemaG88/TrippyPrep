from services.question_service import QuestionService

path = "aptitude/01_foundation/percentage.json"

questions = QuestionService.get_questions(path)

print("Total Questions:", len(questions))

random_questions = QuestionService.get_random_questions(path, 5)

print("\nRandom Questions:")

for q in random_questions:
    print(q["id"])