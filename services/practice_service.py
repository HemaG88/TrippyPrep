import random
from services.question_loader import QuestionLoader


class PracticeService:
    """
    Handles Practice Mode.
    """

    def __init__(self):
        self.loader = QuestionLoader()

    def start_practice(self, json_file, number_of_questions=10):
        """
        Returns random questions for practice.
        """

        questions = self.loader.load_questions(json_file)

        if not questions:
            return []

        number_of_questions = min(number_of_questions, len(questions))

        return random.sample(questions, number_of_questions)