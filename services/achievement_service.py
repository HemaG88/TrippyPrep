from services.analytics_service import AnalyticsService


class AchievementService:

    @classmethod
    def get_badges(cls):

        analytics = AnalyticsService.get_summary()

        badges = []

        if analytics["tests"] >= 1:
            badges.append("🥉 First Practice")

        if analytics["tests"] >= 10:
            badges.append("🥈 Consistent Learner")

        if analytics["tests"] >= 25:
            badges.append("🥇 Placement Warrior")

        if analytics["accuracy"] >= 80:
            badges.append("🎯 Accuracy Master")

        if analytics["accuracy"] >= 90:
            badges.append("👑 Elite Performer")

        return badges