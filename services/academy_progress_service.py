import json
from pathlib import Path


class AcademyProgressService:

    FILE = Path("data/progress/academy_progress.json")

    @classmethod
    def load(cls):

        if cls.FILE.exists():

            with open(cls.FILE, "r", encoding="utf-8") as file:

                return json.load(file)

        return {}

    @classmethod
    def mark_completed(cls, topic):

        data = cls.load()

        data[topic] = True

        with open(cls.FILE, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @classmethod
    def is_completed(cls, topic):

        return cls.load().get(topic, False)

    @classmethod
    def completed_count(cls):

        return len(cls.load())