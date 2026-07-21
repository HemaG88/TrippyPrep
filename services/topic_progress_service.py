import json
from pathlib import Path


class TopicProgressService:

    FILE = Path("data/progress/topic_progress.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():
            return {}

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
    def complete(cls, topic):

        data = cls.load()

        data[topic] = True

        cls.save(data)

    @classmethod
    def is_completed(cls, topic):

        data = cls.load()

        return data.get(topic, False)

    @classmethod
    def completed_count(cls):

        data = cls.load()

        return len(data)