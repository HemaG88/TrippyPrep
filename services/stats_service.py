from services.progress_service import ProgressService
from services.academy_service import AcademyService


class StatsService:

    @classmethod
    def get_dashboard_stats(cls):

        progress = ProgressService.load_progress()

        academy = AcademyService.get_statistics()

        total_questions = progress["total_questions"]

        average = 0

        if total_questions > 0:

            average = round(
                (progress["total_score"] / total_questions) * 100,
                2
            )

        return {

            "tests_completed": progress["tests_completed"],

            "questions_solved": total_questions,

            "correct_answers": progress["total_score"],

            "average_accuracy": average,

            "best_accuracy": progress["best_accuracy"],

            "academy_topics": academy["topics"],

            "academy_questions": academy["questions"]
        }