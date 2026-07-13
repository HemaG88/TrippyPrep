import json
from pathlib import Path
from datetime import datetime


class LeaderboardService:

    FILE = Path("data/progress/leaderboard.json")

    @classmethod
    def save_result(cls, score, total, accuracy):

        if cls.FILE.exists():

            with open(cls.FILE, "r", encoding="utf-8") as file:

                data = json.load(file)

        else:

            data = []

        data.append({

            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),

            "score": score,

            "total": total,

            "accuracy": accuracy

        })

        data = sorted(
            data,
            key=lambda x: x["accuracy"],
            reverse=True
        )[:20]

        with open(cls.FILE, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            return []

        with open(cls.FILE, "r", encoding="utf-8") as file:

            return json.load(file)