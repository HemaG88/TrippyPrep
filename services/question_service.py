from services.question_loader import QuestionLoader
import random


class QuestionService:

    loader = QuestionLoader()

    @classmethod
    def get_questions(cls, path):

        if path.startswith("data/"):
            path = path[5:]

        return cls.loader.load_questions(path)

    @classmethod
    def get_random_questions(cls, path, count=10):

        questions = cls.get_questions(path)

        return random.sample(
            questions,
            min(count, len(questions))
        )

    @classmethod
    def check_answers(cls, questions, answers):

        score = 0
        correct = []
        wrong = []

        for i, q in enumerate(questions):

            user_answer = answers.get(i)

            if user_answer == q["correct_option"]:

                score += 1

                correct.append(q)

            else:

                wrong.append({
                    "question": q["question"],
                    "your_answer": user_answer,
                    "correct_answer": q["correct_option"],
                    "explanation": q["explanation"]
                })

        accuracy = round(
            (score / len(questions)) * 100,
            2
        )

        return {
            "score": score,
            "total": len(questions),
            "accuracy": accuracy,
            "correct": correct,
            "wrong": wrong
        }