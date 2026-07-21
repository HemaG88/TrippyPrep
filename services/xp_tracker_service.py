import json
from pathlib import Path


class XPTrackerService:

    FILE = Path("data/progress/xp.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            return {

                "xp": 0,
                "level": 1
            }

        with open(cls.FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    @classmethod
    def save(cls, data):

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
    def add_xp(cls, points):

        data = cls.load()

        data["xp"] += points

        data["level"] = (data["xp"] // 100) + 1

        cls.save(data)

        return data