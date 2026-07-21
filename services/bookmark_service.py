import json
from pathlib import Path


class BookmarkService:

    FILE = Path("data/progress/bookmarks.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():
            return []

        with open(cls.FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def save(cls, question):

        bookmarks = cls.load()

        question_id = question.get("id")

        for item in bookmarks:

            if item.get("id") == question_id:
                return

        bookmarks.append(question)

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(cls.FILE, "w", encoding="utf-8") as f:

            json.dump(
                bookmarks,
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def remove(cls, question_id):

        bookmarks = [
            q for q in cls.load()
            if q.get("id") != question_id
        ]

        with open(cls.FILE, "w", encoding="utf-8") as f:

            json.dump(
                bookmarks,
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def count(cls):

        return len(cls.load())