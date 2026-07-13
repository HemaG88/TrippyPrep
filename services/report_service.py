from datetime import datetime


class ReportService:

    @classmethod
    def generate_report(cls, result):

        report = {
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "score": result["score"],
            "total": result["total"],
            "accuracy": result["accuracy"],
            "correct": len(result["correct"]),
            "wrong": len(result["wrong"])
        }

        return report