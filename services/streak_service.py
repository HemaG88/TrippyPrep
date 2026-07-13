import json
from pathlib import Path
from datetime import date


class StreakService:

    FILE = Path("data/progress/streak.json")

    @classmethod
    def update_streak(cls):

        if cls.FILE.exists():

            with open(cls.FILE, "r", encoding="utf-8") as file:

                data = json.load(file)

        else:

            data = {
                "last_date": "",
                "streak": 0
            }

        today = str(date.today())

        if data["last_date"] != today:

            data["streak"] += 1
            data["last_date"] = today

        with open(cls.FILE, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @classmethod
    def get_streak(cls):

        if not cls.FILE.exists():

            return 0

        with open(cls.FILE, "r", encoding="utf-8") as file:

            return json.load(file)["streak"]