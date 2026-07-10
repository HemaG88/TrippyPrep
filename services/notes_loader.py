from pathlib import Path


class NotesLoader:

    @staticmethod
    def load(path):

        file = Path(path)

        if not file.exists():
            return "# Notes Coming Soon..."

        return file.read_text(encoding="utf-8")