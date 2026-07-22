import json
from pathlib import Path


class ReportService:

    FILE = Path("storage/progress/reported_questions.json")

    @classmethod
    def load(cls):

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not cls.FILE.exists():

            cls.save([])

            return []

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
                indent=4,
                ensure_ascii=False
            )

    @classmethod
    def report(cls, question):

        reports = cls.load()

        reports.append(question)

        cls.save(reports)

    @classmethod
    def total(cls):

        return len(cls.load())