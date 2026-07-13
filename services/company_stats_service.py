from pathlib import Path
import json


class CompanyStatsService:

    DATA_FOLDER = Path("data/companies")

    @classmethod
    def get_stats(cls):

        stats = {}

        if not cls.DATA_FOLDER.exists():
            return stats

        for company in cls.DATA_FOLDER.iterdir():

            if not company.is_dir():
                continue

            total = 0

            for file in company.glob("*.json"):

                try:

                    with open(file, "r", encoding="utf-8") as f:

                        total += len(json.load(f))

                except Exception:

                    pass

            stats[company.name.replace("_", " ").title()] = total

        return stats