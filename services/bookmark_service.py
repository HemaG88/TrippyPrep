import json
from pathlib import Path


class BookmarkService:

    FILE = Path("storage/progress/bookmarks.json")

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
    def add(cls, question):

        bookmarks = cls.load()

        for item in bookmarks:

            if item.get("id") == question.get("id"):
                return

        bookmarks.append(question)

        cls.save(bookmarks)

    @classmethod
    def remove(cls, question_id):

        bookmarks = [

            q for q in cls.load()

            if q.get("id") != question_id

        ]

        cls.save(bookmarks)

    @classmethod
    def total(cls):

        return len(cls.load())