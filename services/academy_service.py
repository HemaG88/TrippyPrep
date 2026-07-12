from pathlib import Path


class AcademyService:

    DATA_FOLDER = Path("data/aptitude")

    @classmethod
    def get_statistics(cls):

        folders = 0
        topics = 0
        questions = 0

        for folder in cls.DATA_FOLDER.iterdir():

            if folder.is_dir():

                folders += 1

                for file in folder.glob("*.json"):

                    topics += 1

                    try:

                        import json

                        with open(file, "r", encoding="utf-8") as f:

                            questions += len(json.load(f))

                    except Exception:

                        pass

        return {
            "folders": folders,
            "topics": topics,
            "questions": questions
        }