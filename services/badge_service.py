class BadgeService:

    @staticmethod
    def get_badges(score, total):

        badges = []

        if total == 0:
            return badges

        accuracy = (score / total) * 100

        if accuracy == 100:
            badges.append("🏆 Perfect Score")

        if accuracy >= 90:
            badges.append("🔥 Placement Ready")

        if score >= 10:
            badges.append("⚡ Fast Learner")

        if score >= 20:
            badges.append("💎 Quiz Master")

        return badges