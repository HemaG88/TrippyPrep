import json
from pathlib import Path


class CompanyService:

    DATA_FOLDER = Path("data/companies")

    @classmethod
    def get_companies(cls):

        companies = []

        if cls.DATA_FOLDER.exists():

            for folder in cls.DATA_FOLDER.iterdir():

                if folder.is_dir():

                    companies.append(
                        folder.name.replace("_", " ").title()
                    )

        return sorted(companies)

    @classmethod
    def load_company_questions(cls, company, section):

        company = company.lower().replace(" ", "_")

        file_path = (
            cls.DATA_FOLDER /
            company /
            f"{section.lower()}.json"
        )

        if not file_path.exists():

            return []

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read().strip()

                if content == "":

                    return []

                return json.loads(content)

        except Exception:

            return []