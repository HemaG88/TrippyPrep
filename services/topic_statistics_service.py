import json
from pathlib import Path


class TopicStatisticsService:

    @staticmethod
    def get_statistics(file_path):

        path = Path(file_path)

        if not path.exists():

            return {
                "questions": 0,
                "easy": 0,
                "medium": 0,
                "hard": 0
            }

        with open(path, "r", encoding="utf-8") as f:

            questions = json.load(f)

        easy = 0
        medium = 0
        hard = 0

        for q in questions:

            difficulty = q.get(
                "difficulty",
                ""
            ).lower()

            if difficulty == "easy":

                easy += 1

            elif difficulty == "medium":

                medium += 1

            elif difficulty == "hard":

                hard += 1

        return {

            "questions": len(questions),

            "easy": easy,

            "medium": medium,

            "hard": hard
        }