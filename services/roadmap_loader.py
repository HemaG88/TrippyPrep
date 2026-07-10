import json


class RoadmapLoader:

    @staticmethod
    def load_aptitude():

        with open(
            "data/academy/aptitude_roadmap.json",
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)