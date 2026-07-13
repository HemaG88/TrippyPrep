from pathlib import Path


class TopicService:

    DATA_FOLDER = Path("data/aptitude")

    @classmethod
    def get_all_topics(cls):

        topics = []

        for folder in sorted(cls.DATA_FOLDER.iterdir()):

            if folder.is_dir():

                for file in sorted(folder.glob("*.json")):

                    topics.append({
                        "name": file.stem.replace("_", " ").title(),
                        "path": str(file.relative_to("data")).replace("\\", "/")
                    })
        return topics