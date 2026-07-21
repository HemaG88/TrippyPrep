import random


class QuizEngine:

    def __init__(self, questions):

        self.questions = questions.copy()
        random.shuffle(self.questions)

        self.current_index = 0
        self.answers = {}
        self.review = set()
        self.score = 0

    def total_questions(self):
        return len(self.questions)

    def current_number(self):
        return self.current_index + 1

    def current_question(self):
        return self.questions[self.current_index]

    def goto_question(self, index):
        self.current_index = index

    def next_question(self):
        if self.current_index < len(self.questions) - 1:
            self.current_index += 1

    def previous_question(self):
        if self.current_index > 0:
            self.current_index -= 1

    def has_next(self):
        return self.current_index < len(self.questions)

    def check_answer(self, selected):

        question = self.current_question()

        self.answers[self.current_index] = selected

        correct = selected == question["correct_option"]

        if correct:
            self.score += 1

        return correct

    def get_score(self):
        return self.score

    def is_answered(self, index):
        return index in self.answers

    def mark_review(self):
        self.review.add(self.current_index)

    def unmark_review(self):
        self.review.discard(self.current_index)

    def is_review(self, index):
        return index in self.review
