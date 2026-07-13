import json
from pathlib import Path


class ProgressService:

    FILE = Path("data/progress/user_progress.json")

    @classmethod
    def load_progress(cls):

        default = {

            "tests_completed": 0,

            "total_score": 0,

            "total_questions": 0,

            "best_accuracy": 0
        }

        if not cls.FILE.exists():

            with open(cls.FILE, "w", encoding="utf-8") as file:

                json.dump(default, file, indent=4)

            return default

        try:

            with open(cls.FILE, "r", encoding="utf-8") as file:

                content = file.read().strip()

                if content == "":

                    return default

                return json.loads(content)

        except Exception:

            return default

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