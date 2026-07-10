from services.question_loader import QuestionLoader

loader = QuestionLoader()

json_file = "aptitude/01_foundation/number_system.json"

# Load all questions
questions = loader.load_questions(json_file)

print("=" * 60)
print("           TrippyPrep Question Loader Test")
print("=" * 60)

print(f"Academy          : {loader.get_academy_name(json_file)}")
print(f"Level            : {loader.get_level_name(json_file)}")
print(f"Topic            : {loader.get_topic_name(json_file)}")
print(f"Total Questions  : {loader.total_questions(json_file)}")

print("\nFirst Question")
print("-" * 60)
print(questions[0]["question"])

correct_index = questions[0]["correct_option"] - 1

print("\nCorrect Answer")
print("-" * 60)
print(questions[0]["options"][correct_index])

print("\nRandom Question Test")
print("-" * 60)

random_questions = loader.get_random_questions(json_file, 1)

for q in random_questions:
    print(q["question"])