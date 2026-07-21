from pathlib import Path
import json


class CompanyService:

    DATA_DIR = Path("data/companies")

    @classmethod
    def get_companies(cls):

        companies = []

        if not cls.DATA_DIR.exists():
            return companies

        for folder in cls.DATA_DIR.iterdir():

            if folder.is_dir():

                companies.append(
                    folder.name.replace("_", " ").title()
                )

        return sorted(companies)

    @staticmethod
    def get_companies_for_question(question_file):

        path = Path(question_file)

        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as f:
            questions = json.load(f)

        companies = set()

        for question in questions:

            value = question.get("companies")

            if not value:
                continue

            if isinstance(value, list):
                companies.update(value)
            else:
                companies.add(value)

        return sorted(companies)