import json
from pathlib import Path


class ProgressService:

    FILE = Path("storage/progress/user_progress.json")

    DEFAULT = {
        "tests_completed": 0,
        "total_score": 0,
        "total_questions": 0,
        "best_accuracy": 0
    }

    @classmethod
    def load_progress(cls):

        cls.FILE.parent.mkdir(parents=True, exist_ok=True)

        if not cls.FILE.exists():

            with open(cls.FILE, "w", encoding="utf-8") as file:
                json.dump(cls.DEFAULT, file, indent=4)

            return cls.DEFAULT.copy()

        try:

            with open(cls.FILE, "r", encoding="utf-8") as file:

                data = json.load(file)

                for key, value in cls.DEFAULT.items():
                    data.setdefault(key, value)

                return data

        except Exception:

            return cls.DEFAULT.copy()

    @classmethod
    def save_progress(cls, progress):

        cls.FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(cls.FILE, "w", encoding="utf-8") as file:
            json.dump(progress, file, indent=4)

    @classmethod
    def save_result(cls, score, total, accuracy):

        progress = cls.load_progress()

        progress["tests_completed"] += 1
        progress["total_score"] += score
        progress["total_questions"] += total

        if accuracy > progress["best_accuracy"]:
            progress["best_accuracy"] = accuracy

        cls.save_progress(progress)