import json
from pathlib import Path


class LearningService:

    @staticmethod
    def load_topic(file_path):

        path = Path(file_path)

        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as file:

            return json.load(file)

    @staticmethod
    def get_notes(file_path):

        questions = LearningService.load_topic(file_path)

        notes = []

        for question in questions:

            notes.append({

                "question": question.get("question", ""),

                "formula": question.get("formula", ""),

                "shortcut": question.get("shortcut", ""),

                "tip": question.get("learning_tip", ""),

                "explanation": question.get("explanation", "")

            })

        return notes