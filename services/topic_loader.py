import json


class TopicLoader:

    @staticmethod
    def load_topics():

        with open(
            "data/aptitude/aptitude_topics.json",
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)