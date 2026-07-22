from services.progress_service import ProgressService
from services.xp_tracker_service import XPTrackerService
from services.bookmark_service import BookmarkService
from services.report_service import ReportService
from services.streak_service import StreakService


class StatisticsService:

    @staticmethod
    def get_statistics():

        progress = ProgressService.load_progress()

        xp = XPTrackerService.load()

        return {

            "tests": progress["tests_completed"],

            "questions": progress["total_questions"],

            "best_accuracy": progress["best_accuracy"],

            "xp": xp["xp"],

            "level": xp["level"],

            "bookmarks": BookmarkService.total(),

            "reports": ReportService.total(),

            "streak": StreakService.current()

        }