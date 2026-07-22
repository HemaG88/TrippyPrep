import json
from pathlib import Path


class SettingsService:

    FILE = Path("storage/settings.json")

    @classmethod
    def load(cls):

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        default = {

            "dark_mode": True,

            "sound": True,

            "notifications": True,

            "daily_goal": 20

        }

        if not cls.FILE.exists():

            cls.save(default)

            return default

        try:

            with open(
                cls.FILE,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except Exception:

            cls.save(default)

            return default

    @classmethod
    def save(cls, data):

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            cls.FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )