import json
from pathlib import Path


class ReportService:

    FILE = Path("data/progress/reported_questions.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():
            return []

        with open(cls.FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def report(cls, question):

        reports = cls.load()

        question_id = question.get("id")

        for item in reports:

            if item.get("id") == question_id:
                return

        reports.append(question)

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(cls.FILE, "w", encoding="utf-8") as f:

            json.dump(
                reports,
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def count(cls):

        return len(cls.load())