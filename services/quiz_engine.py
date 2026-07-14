class QuizEngine:

    def __init__(self, questions):

        self.questions = questions
        self.current_index = 0
        self.score = 0

        self.answers = {}

    def current_question(self):

        if self.current_index >= len(self.questions):
            return None

        return self.questions[self.current_index]

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

    def next_question(self):

        self.current_index += 1

    def previous_question(self):

        if self.current_index > 0:
            self.current_index -= 1

    def goto_question(self, index):

        if 0 <= index < len(self.questions):
            self.current_index = index

    def has_next(self):

        return self.current_index < len(self.questions)

    def total_questions(self):

        return len(self.questions)

    def current_number(self):

        return self.current_index + 1

    def get_score(self):

        return self.score

    def is_answered(self, index):

        return index in self.answers