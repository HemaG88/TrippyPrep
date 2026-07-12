from services.progress_service import ProgressService


class RecommendationService:

    @classmethod
    def get_recommendation(cls):

        progress = ProgressService.load_progress()

        if progress["tests_completed"] == 0:
            return "Start your first practice test."

        total = progress["total_questions"]

        accuracy = 0

        if total > 0:
            accuracy = (
                progress["total_score"] / total
            ) * 100

        if accuracy >= 90:
            return "Excellent! Start Company-wise Preparation."

        elif accuracy >= 75:
            return "Good progress. Start Mock Interviews."

        elif accuracy >= 60:
            return "Focus on Weak Topics and Practice More."

        return "Revise Fundamentals before attempting Mock Tests."