import json
from pathlib import Path


class ProgressService:

    FILE = Path("data/progress/user_progress.json")

    @classmethod
    def load_progress(cls):

        if not cls.FILE.exists():

            return {
                "tests_completed": 0,
                "total_score": 0,
                "total_questions": 0,
                "best_accuracy": 0
            }

        with open(cls.FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    @classmethod
    def save_result(cls, score, total, accuracy):

        progress = cls.load_progress()

        progress["tests_completed"] += 1
        progress["total_score"] += score
        progress["total_questions"] += total

        if accuracy > progress["best_accuracy"]:
            progress["best_accuracy"] = accuracy

        with open(cls.FILE, "w", encoding="utf-8") as file:

            json.dump(
                progress,
                file,
                indent=4
            )