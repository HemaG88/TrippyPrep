from utils.json_loader import load_folder_questions


path = "data/aptitude/02_arithmetic"


questions = load_folder_questions(path)


print("Total Questions:", len(questions))


if questions:
    print("\nFirst Question:")
    print(questions[0])