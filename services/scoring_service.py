class ScoringService:
    """
    Handles scoring and result calculation.
    """

    def calculate_score(self, questions, user_answers):
        """
        Calculate user's score.

        Parameters:
            questions (list): Question objects.
            user_answers (list): Selected option numbers.

        Returns:
            dict
        """

        total_questions = len(questions)
        correct = 0
        wrong = 0

        results = []

        for question, answer in zip(questions, user_answers):

            is_correct = answer == question["correct_option"]

            if is_correct:
                correct += 1
            else:
                wrong += 1

            results.append({
                "question": question["question"],
                "selected_option": answer,
                "correct_option": question["correct_option"],
                "is_correct": is_correct
            })

        percentage = 0

        if total_questions > 0:
            percentage = round((correct / total_questions) * 100, 2)

        return {
            "total": total_questions,
            "correct": correct,
            "wrong": wrong,
            "percentage": percentage,
            "results": results
        }