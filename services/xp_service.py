class XPService:

    @staticmethod
    def calculate(score, total):

        if total == 0:
            return 0

        accuracy = (score / total) * 100

        xp = score * 10

        if accuracy >= 90:
            xp += 100

        elif accuracy >= 75:
            xp += 60

        elif accuracy >= 50:
            xp += 30

        return xp

    @staticmethod
    def level(xp):

        if xp >= 5000:
            return "Placement Master"

        elif xp >= 3500:
            return "Expert"

        elif xp >= 2000:
            return "Advanced"

        elif xp >= 1000:
            return "Intermediate"

        elif xp >= 300:
            return "Beginner"

        return "Starter"