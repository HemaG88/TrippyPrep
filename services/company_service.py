from pathlib import Path


class CompanyService:

    DATA_DIR = Path("data/companies")

    @classmethod
    def get_companies(cls):

        if not cls.DATA_DIR.exists():
            return []

        companies = []

        for folder in cls.DATA_DIR.iterdir():

            if folder.is_dir():

                companies.append(
                    folder.name.replace("_", " ").title()
                )

        return sorted(companies)

    @classmethod
    def get_company_topics(cls, company):

        company = company.lower().replace(" ", "_")

        folder = cls.DATA_DIR / company

        if not folder.exists():
            return []

        topics = []

        for file in folder.glob("*.json"):

            topics.append(
                file.stem.replace("_", " ").title()
            )

        return sorted(topics)