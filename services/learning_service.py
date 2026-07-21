import json
from pathlib import Path


class LearningService:

    @staticmethod
    def get_notes(file_path):

        path = Path(file_path)

        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as f:
            questions = json.load(f)

        notes = []

        for q in questions:

            notes.append({
                "question": q.get("question", ""),
                "formula": q.get("formula", ""),
                "shortcut": q.get("shortcut", ""),
                "tip": q.get("learning_tip", ""),
                "explanation": q.get("explanation", "")
            })

        return notes