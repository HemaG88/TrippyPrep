from services.question_loader import QuestionLoader


class StatisticsService:
    """
    Calculates statistics for question datasets.
    """

    def __init__(self):
        self.loader = QuestionLoader()

    def get_topic_statistics(self, json_file):
        questions = self.loader.load_questions(json_file)

        stats = {
            "total": len(questions),
            "easy": 0,
            "medium": 0,
            "hard": 0
        }

        for question in questions:
            difficulty = question["difficulty"].lower()

            if difficulty == "easy":
                stats["easy"] += 1
            elif difficulty == "medium":
                stats["medium"] += 1
            elif difficulty == "hard":
                stats["hard"] += 1

        return stats