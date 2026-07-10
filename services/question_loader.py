import json
import random
from pathlib import Path


class QuestionLoader:

    def __init__(self):
        self.data_folder = Path("data")

    def load_questions(self, json_file):

        file_path = self.data_folder / json_file

        print("\n==============================")
        print("Loading File:")
        print(file_path)
        print("==============================\n")

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        with open(file_path, "r", encoding="utf-8") as file:

            content = file.read()

        if content.strip() == "":
            raise Exception(f"JSON file is EMPTY:\n{file_path}")

        return json.loads(content)

    def total_questions(self, json_file):
        return len(self.load_questions(json_file))

    def get_random_questions(self, json_file, count=5):

        questions = self.load_questions(json_file)

        return random.sample(
            questions,
            min(count, len(questions))
        )