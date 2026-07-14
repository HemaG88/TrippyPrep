import json
from pathlib import Path
class JSONLoader:
    """Loads question data from a JSON file."""

    @staticmethod
    def load(file_path):

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)