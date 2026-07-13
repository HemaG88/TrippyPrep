import random

from services.question_service import QuestionService


class TestService:

    @classmethod
    def generate_mock_test(cls, topics, questions_per_topic=5):

        test_questions = []

        for topic in topics:

            try:

                qs = QuestionService.get_questions(topic)

                qs = random.sample(
                    qs,
                    min(questions_per_topic, len(qs))
                )

                test_questions.extend(qs)

            except Exception:

                pass

        random.shuffle(test_questions)

        return test_questions