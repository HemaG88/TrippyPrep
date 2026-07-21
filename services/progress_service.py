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
                "best_accuracy": 0,
            }

        with open(cls.FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    @classmethod
    def save_progress(cls, data):

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(cls.FILE, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
            )

    @classmethod
    def save_result(
        cls,
        score,
        total_questions,
        accuracy,
    ):

        progress = cls.load_progress()

        progress["tests_completed"] += 1

        progress["total_score"] += score

        progress["total_questions"] += total_questions

        progress["best_accuracy"] = max(
            progress["best_accuracy"],
            accuracy,
        )

        cls.save_progress(progress)