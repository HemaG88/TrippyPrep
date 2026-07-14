class QuizEngine:

    def __init__(self, questions):

        self.questions = questions
        self.current_index = 0
        self.score = 0

        self.answers = {}
        self.review = set()

    # ==========================================
    # Current Question
    # ==========================================

    def current_question(self):

        if self.current_index >= len(self.questions):
            return None

        return self.questions[self.current_index]

    # ==========================================
    # Answer
    # ==========================================

    def check_answer(self, selected_option):

        question = self.current_question()

        correct = (
            str(selected_option)
            == str(question["correct_option"])
        )

        self.answers[self.current_index] = {
            "selected": selected_option,
            "correct": question["correct_option"],
            "is_correct": correct
        }

        if correct:
            self.score += 1

        return correct

    # ==========================================
    # Navigation
    # ==========================================

    def next_question(self):

        if self.current_index < len(self.questions):
            self.current_index += 1

    def previous_question(self):

        if self.current_index > 0:
            self.current_index -= 1

    def goto_question(self, index):

        if 0 <= index < len(self.questions):
            self.current_index = index

    # ==========================================
    # Review
    # ==========================================

    def mark_review(self):

        self.review.add(self.current_index)

    def unmark_review(self):

        self.review.discard(self.current_index)

    def is_review(self, index):

        return index in self.review

    # ==========================================
    # Status
    # ==========================================

    def is_answered(self, index):

        return index in self.answers

    def has_previous(self):

        return self.current_index > 0

    def has_next(self):

        return self.current_index < len(self.questions)

    # ==========================================
    # Stats
    # ==========================================

    def total_questions(self):

        return len(self.questions)

    def current_number(self):

        return self.current_index + 1

    def get_score(self):

        return self.score
        # ==========================================
    # Statistics
    # ==========================================

    def answered_count(self):

        return len(self.answers)

    def review_count(self):

        return len(self.review)

    def remaining_count(self):

        return (
            len(self.questions)
            - len(self.answers)
        )

    def current_score(self):

        return self.score
        # ==========================================
    # Navigation Status
    # ==========================================

    def visited_count(self):

        return max(self.current_index + 1, len(self.answers))

    def skipped_count(self):

        return self.visited_count() - len(self.answers)

    def answered_correct(self):

        return self.score

    def answered_wrong(self):

        return len(self.answers) - self.score