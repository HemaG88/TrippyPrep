from services.question_loader import QuestionLoader


class QuestionService:

    loader = QuestionLoader()

    @classmethod
    def get_questions(cls, path):

        if path.startswith("data/"):

            path = path[5:]

        return cls.loader.load_questions(path)