class ResultAnalysisService:

    @staticmethod
    def analyze(quiz):

        total = quiz.total_questions()
        score = quiz.get_score()

        accuracy = 0

        if total > 0:
            accuracy = round(
                (score / total) * 100,
                2
            )

        performance = "Needs Practice"

        if accuracy >= 90:
            performance = "Excellent"

        elif accuracy >= 75:
            performance = "Very Good"

        elif accuracy >= 60:
            performance = "Good"

        return {

            "score": score,

            "total": total,

            "accuracy": accuracy,

            "correct": score,

            "wrong": total - score,

            "answered": quiz.answered_count(),

            "review": quiz.review_count(),

            "remaining": quiz.remaining_count(),

            "performance": performance
        }