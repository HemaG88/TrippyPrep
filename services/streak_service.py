import json
from pathlib import Path
from datetime import date


class StreakService:

    FILE = Path("storage/progress/streak.json")

    @classmethod
    def load(cls):

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not cls.FILE.exists():

            data = {

                "streak": 0,

                "last_date": ""

            }

            cls.save(data)

            return data

        with open(
            cls.FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    @classmethod
    def save(cls, data):

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            cls.FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    @classmethod
    def update(cls):

        data = cls.load()

        today = str(date.today())

        if data["last_date"] != today:

            data["streak"] += 1

            data["last_date"] = today

            cls.save(data)

        return data

    @classmethod
    def current(cls):

        return cls.load()["streak"]