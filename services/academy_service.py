from pathlib import Path
import json


class AcademyService:

    DATA_PATH = Path("data")

    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return []

    @classmethod
    def get_academies(cls):
        file_path = cls.DATA_PATH / "academy.json"
        return cls.load_json(file_path)

    @classmethod
    def get_aptitude_topics(cls):
        file_path = cls.DATA_PATH / "aptitude" / "aptitude_topics.json"
        return cls.load_json(file_path)

    @classmethod
    def get_statistics(cls):

        topics = cls.get_aptitude_topics()

        return {
            "topics": len(topics),
            "questions": len(topics) * 25
        }
    @classmethod
    def get_statistics(cls):

        topics = cls.get_aptitude_topics()

        return {

            "topics": len(topics),

            "questions": len(topics) * 25
        }
@classmethod
def search_topics(cls, keyword):

    keyword = keyword.lower()

    topics = cls.get_aptitude_topics()

    return [

        topic

        for topic in topics

        if keyword in topic["name"].lower()

    ]