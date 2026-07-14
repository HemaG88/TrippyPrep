import streamlit as st

from services.json_loader import JSONLoader
from services.quiz_engine import QuizEngine
from services.progress_service import ProgressService


def show():

    # ---------------------------------------
    # Session State
    # ---------------------------------------

    if "selected_question_file" not in st.session_state:
        st.error("No topic selected.")
        return

    if "quiz_engine" not in st.session_state:

        questions = JSONLoader.load(
            st.session_state.selected_question_file
        )

        st.session_state.quiz_engine = QuizEngine(questions)

    if "answer_submitted" not in st.session_state:
        st.session_state.answer_submitted = False

    if "last_answer_correct" not in st.session_state:
        st.session_state.last_answer_correct = False

    quiz = st.session_state.quiz_engine
    # ======================================
# Sidebar Question Palette
# ======================================

st.sidebar.title("📋 Question Palette")

for i in range(quiz.total_questions()):

    label = f"Q{i+1}"

    if quiz.is_answered(i):
        label = "✅ " + label

    if st.sidebar.button(
        label,
        key=f"palette_{i}",
        use_container_width=True
    ):

        quiz.goto_question(i)

        st.session_state.answer_submitted = False

        st.rerun()

    # ---------------------------------------
    # Quiz Finished
    # ---------------------------------------

    if not quiz.has_next():

        score = quiz.get_score()
        total = quiz.total_questions()

        accuracy = 0

        if total > 0:
            accuracy = round((score / total) * 100, 2)

        ProgressService.save_result(
            score,
            total,
            accuracy
        )

        st.balloons()

        st.success("🎉 Quiz Completed")

        c1, c2, c3 = st.columns(3)

        c1.metric("Score", f"{score}/{total}")
        c2.metric("Accuracy", f"{accuracy}%")
        c3.metric("Correct", score)

        st.divider()

        if st.button("⬅ Back To Topics", use_container_width=True):

            del st.session_state.quiz_engine

            st.session_state.selected_question_file = None
            st.session_state.answer_submitted = False

            st.rerun()

   return

    # ---------------------------------------
    # Current Question
    # ---------------------------------------

    question = quiz.current_question()

    st.title(
        f"Question {quiz.current_number()} / {quiz.total_questions()}"
    )

    st.progress(
        quiz.current_number() / quiz.total_questions()
    )

    st.write("## " + question["question"])

    answer = st.radio(
        "Choose your answer",
        question["options"],
        index=None,
        disabled=st.session_state.answer_submitted,
        key=f"answer_{quiz.current_number()}"
    )

    # ---------------------------------------
    # Submit
    # ---------------------------------------

    if (
        not st.session_state.answer_submitted
        and st.button("Submit", use_container_width=True)
    ):

        if answer is None:

            st.warning("Please select an option.")

            st.stop()

        selected = question["options"].index(answer) + 1

        correct = quiz.check_answer(selected)

        st.session_state.last_answer_correct = correct
        st.session_state.answer_submitted = True

        st.rerun()

    # ---------------------------------------
    # Review Section
    # ---------------------------------------

    if st.session_state.answer_submitted:

        if st.session_state.last_answer_correct:

            st.success("✅ Correct Answer")

        else:

            st.error("❌ Wrong Answer")

        st.divider()

        st.subheader("📖 Explanation")
        st.info(question["explanation"])

        if question.get("formula"):

            st.subheader("📐 Formula")
            st.code(question["formula"])

        if question.get("shortcut"):

            st.subheader("⚡ Shortcut")
            st.success(question["shortcut"])

        if question.get("learning_tip"):

            st.subheader("💡 Learning Tip")
            st.info(question["learning_tip"])

        if question.get("estimated_time"):

            st.subheader("⏱ Estimated Time")
            st.write(question["estimated_time"])

        if question.get("companies"):

            st.subheader("🏢 Frequently Asked In")

            companies = question["companies"]

            if isinstance(companies, list):

                st.write(", ".join(companies))

            else:

                st.write(companies)

        st.divider()

        if st.button("Next Question ➜", use_container_width=True):

            quiz.next_question()

            st.session_state.answer_submitted = False

            st.rerun()