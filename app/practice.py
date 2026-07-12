import streamlit as st
from services.question_service import QuestionService


def show():

    st.title("✍ Practice")

    path = st.selectbox(
        "Select Topic",
        [
            "aptitude/01_foundation/percentage.json",
            "aptitude/01_foundation/profit_loss.json",
            "aptitude/01_foundation/average.json",
            "aptitude/02_arithmetic/ages.json",
            "aptitude/02_arithmetic/time_and_work.json",
        ],
    )

    # -----------------------------
    # Session State
    # -----------------------------

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "current" not in st.session_state:
        st.session_state.current = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if "test_started" not in st.session_state:
        st.session_state.test_started = False

    # -----------------------------
    # Start Practice
    # -----------------------------

    if st.button("🚀 Start Practice"):

        st.session_state.questions = QuestionService.get_random_questions(path, 10)

        st.session_state.current = 0
        st.session_state.answers = {}
        st.session_state.test_started = True

        st.rerun()

    # -----------------------------
    # Practice Screen
    # -----------------------------

    if st.session_state.test_started:

        questions = st.session_state.questions

        if st.session_state.current < len(questions):

            q = questions[st.session_state.current]

            st.progress(
                (st.session_state.current + 1) / len(questions)
            )

            st.subheader(
                f"Question {st.session_state.current + 1} / {len(questions)}"
            )

            st.write(q["question"])

            answer = st.radio(
                "Choose Answer",
                q["options"],
                key=f"question_{st.session_state.current}",
            )

            if st.button("Next"):

                st.session_state.answers[
                    st.session_state.current
                ] = answer

                st.session_state.current += 1

                st.rerun()

        else:

            result = QuestionService.check_answers(
                questions,
                st.session_state.answers
            )

            # -----------------------------
            # Dashboard Data
            # -----------------------------

            st.session_state.last_score = result["score"]
            st.session_state.last_total = result["total"]
            st.session_state.last_accuracy = result["accuracy"]

            st.session_state.tests_completed = (
                st.session_state.get("tests_completed", 0) + 1
            )

            # -----------------------------
            # Result
            # -----------------------------

            st.success("🎉 Practice Test Completed")

            st.markdown("---")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Score",
                    f"{result['score']}/{result['total']}"
                )

            with c2:
                st.metric(
                    "Correct",
                    len(result["correct"])
                )

            with c3:
                st.metric(
                    "Accuracy",
                    f"{result['accuracy']}%"
                )

            st.markdown("---")

            st.subheader("❌ Wrong Answers Review")

            if len(result["wrong"]) == 0:

                st.success("Excellent! All answers are correct. 🎉")

            else:

                for i, q in enumerate(result["wrong"], start=1):

                    with st.expander(f"Question {i}"):

                        st.write("**Question**")
                        st.write(q["question"])

                        st.write("**Your Answer**")
                        st.error(q["your_answer"])

                        st.write("**Correct Answer**")
                        st.success(q["correct_answer"])

                        st.write("**Explanation**")
                        st.info(q["explanation"])

            st.markdown("---")

            if st.button("🔄 Practice Again"):

                st.session_state.questions = []
                st.session_state.answers = {}
                st.session_state.current = 0
                st.session_state.test_started = False

                st.rerun()