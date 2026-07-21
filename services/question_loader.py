import json
import random
from pathlib import Path


class QuestionLoader:

    DATA_DIR = Path(".")

    @classmethod
    def load_questions(cls, json_file):

        path = Path(json_file)

        if not path.is_absolute():
            path = cls.DATA_DIR / path

        if not path.exists():
            raise FileNotFoundError(path)

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def total_questions(cls, json_file):
        return len(cls.load_questions(json_file))

    @classmethod
    def get_random_questions(cls, json_file, count=5):

        questions = cls.load_questions(json_file)

        return random.sample(
            questions,
            min(count, len(questions))
        )