import json
from pathlib import Path


class RecentActivityService:

    FILE = Path("data/progress/recent_activity.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            return []

        with open(cls.FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    @classmethod
    def save(cls, activity):

        activities = cls.load()

        activities.insert(0, activity)

        activities = activities[:20]

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(cls.FILE, "w", encoding="utf-8") as f:

            json.dump(
                activities,
                f,
                indent=4,
            )