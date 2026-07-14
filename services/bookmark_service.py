import json
from pathlib import Path


class BookmarkService:

    FILE = Path("storage/bookmarks.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            cls.FILE.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(cls.FILE, "w") as f:

                json.dump([], f)

        with open(cls.FILE, "r") as f:

            return json.load(f)

    @classmethod
    def save(cls, question):

        bookmarks = cls.load()

        if question["id"] not in [q["id"] for q in bookmarks]:

            bookmarks.append(question)

            with open(cls.FILE, "w") as f:

                json.dump(
                    bookmarks,
                    f,
                    indent=4
                )