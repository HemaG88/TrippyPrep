from services.progress_service import ProgressService
from services.xp_tracker_service import XPTrackerService
from services.bookmark_service import BookmarkService
from services.report_service import ReportService
from services.recent_activity_service import RecentActivityService
from services.topic_progress_service import TopicProgressService


class DashboardService:

    @classmethod
    def get_dashboard_data(cls):

        progress = ProgressService.load_progress()

        xp = XPTrackerService.load()

        activities = RecentActivityService.load()

        return {

            "tests_completed":
                progress["tests_completed"],

            "questions_solved":
                progress["total_questions"],

            "correct_answers":
                progress["total_score"],

            "best_accuracy":
                progress["best_accuracy"],

            "xp":
                xp["xp"],

            "level":
                xp["level"],

            "completed_topics":
                TopicProgressService.completed_count(),

            "bookmarks":
                BookmarkService.count(),

            "reports":
                ReportService.count(),

            "recent":
                activities[:5],
        }