from services.progress_service import ProgressService


class RecommendationService:

    @classmethod
    def get_recommendations(cls):

        progress = ProgressService.load_progress()

        recommendations = []

        if progress["tests_completed"] == 0:

            recommendations.append(
                "Start with Number System."
            )

            recommendations.append(
                "Complete your first quiz."
            )

            recommendations.append(
                "Read Learning Mode before Practice."
            )

            return recommendations

        if progress["best_accuracy"] < 60:

            recommendations.append(
                "Revise completed topics."
            )

            recommendations.append(
                "Practice Easy level questions."
            )

        elif progress["best_accuracy"] < 80:

            recommendations.append(
                "Move to Medium level."
            )

            recommendations.append(
                "Attempt Mixed Practice."
            )

        else:

            recommendations.append(
                "Start Company Preparation."
            )

            recommendations.append(
                "Attempt Mock Interviews."
            )

        recommendations.append(
            "Maintain a daily practice streak."
        )

        return recommendations