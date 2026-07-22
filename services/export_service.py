import json
from pathlib import Path

from services.progress_service import ProgressService
from services.xp_tracker_service import XPTrackerService
from services.streak_service import StreakService


class ExportService:

    @staticmethod
    def export():

        return {

            "progress": ProgressService.load_progress(),

            "xp": XPTrackerService.load(),

            "streak": StreakService.load()

        }

    @staticmethod
    def save():

        data = ExportService.export()

        output = Path("storage/trippyprep_backup.json")

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        return output