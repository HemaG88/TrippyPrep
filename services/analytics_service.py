from collections import Counter
from services.progress_service import ProgressService


class AnalyticsService:

    @classmethod
    def get_summary(cls):

        progress = ProgressService.load_progress()

        total = progress["total_questions"]
        score = progress["total_score"]

        accuracy = 0

        if total > 0:
            accuracy = round((score / total) * 100, 2)

        level = "Beginner"

        if accuracy >= 90:
            level = "Expert"
        elif accuracy >= 75:
            level = "Advanced"
        elif accuracy >= 60:
            level = "Intermediate"

        return {
            "accuracy": accuracy,
            "level": level,
            "tests": progress["tests_completed"],
            "questions": total,
            "correct": score
        }