import time
import streamlit as st

from services.json_loader import JSONLoader
from services.quiz_engine import QuizEngine
from services.progress_service import ProgressService
from services.bookmark_service import BookmarkService


def show():

    # ==========================================================
    # Session State
    # ==========================================================

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

    if "question_start_time" not in st.session_state:
        st.session_state.question_start_time = time.time()

    quiz = st.session_state.quiz_engine

    # ==========================================================
    # Sidebar
    # ==========================================================

    st.sidebar.title("📋 Question Palette")

    for i in range(quiz.total_questions()):

        label = f"Q{i + 1}"

        if quiz.is_review(i):
            label = "🟡 " + label

        elif quiz.is_answered(i):
            label = "🟢 " + label

        if st.sidebar.button(
            label,
            key=f"palette_{i}",
            use_container_width=True
        ):

            quiz.goto_question(i)

            st.session_state.answer_submitted = False

            st.session_state.question_start_time = time.time()

            st.rerun()

    # ==========================================================
    # Quiz Completed
    # ==========================================================

    if not quiz.has_next():

        score = quiz.get_score()

        total = quiz.total_questions()

        accuracy = 0

        if total > 0:

            accuracy = round(
                (score / total) * 100,
                2
            )

        ProgressService.save_result(
            score,
            total,
            accuracy
        )

        st.session_state.quiz_completed = True

        st.rerun()

        return

    # ==========================================================
    # Current Question
    # ==========================================================

    question = quiz.current_question()

    st.title(
        f"Question {quiz.current_number()} / {quiz.total_questions()}"
    )

    st.progress(
        quiz.current_number() /
        quiz.total_questions()
    )

    st.caption(
        f"Question {quiz.current_number()} of {quiz.total_questions()}"
    )

    elapsed = int(
        time.time() -
        st.session_state.question_start_time
    )

    minutes = elapsed // 60

    seconds = elapsed % 60

    st.info(
        f"⏱ {minutes:02d}:{seconds:02d}"
    )

    st.write("## " + question["question"])

    answer = st.radio(
        "Choose your answer",
        question["options"],
        index=None,
        disabled=st.session_state.answer_submitted,
        key=f"answer_{quiz.current_number()}"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button(
            "🟡 Mark For Review",
            use_container_width=True
        ):

            quiz.mark_review()

            st.success(
                "Question marked for review."
            )

    with c2:

        if quiz.is_review(
            quiz.current_index
        ):

            if st.button(
                "❌ Remove Review",
                use_container_width=True
            ):

                quiz.unmark_review()

                st.rerun()

    with c3:

     if st.button(
        "⭐ Bookmark",
        use_container_width=True
    ):

        BookmarkService.save(question)

        st.success(
            "Question bookmarked."
        )          

    st.divider()


    if (
        not st.session_state.answer_submitted
        and st.button(
            "Submit",
            use_container_width=True
        )
    ):

        if answer is None:

            st.warning(
                "Please select an answer."
            )

            st.stop()

        selected = (
            question["options"].index(answer)
            + 1
        )

        correct = quiz.check_answer(
            selected
        )

        st.session_state.last_answer_correct = correct

        st.session_state.answer_submitted = True

        st.rerun()  
            # ==========================================================
    # Review Section
    # ==========================================================

    if st.session_state.answer_submitted:

        if st.session_state.last_answer_correct:

            st.success("✅ Correct Answer")

        else:

            st.error("❌ Wrong Answer")

        st.divider()

        st.subheader("📖 Explanation")

        st.info(
            question.get(
                "explanation",
                "No explanation available."
            )
        )

        if question.get("formula"):

            st.subheader("📐 Formula")

            st.code(
                question["formula"]
            )

        if question.get("shortcut"):

            st.subheader("⚡ Shortcut")

            st.success(
                question["shortcut"]
            )

        if question.get("learning_tip"):

            st.subheader("💡 Learning Tip")

            st.info(
                question["learning_tip"]
            )

        if question.get("estimated_time"):

            st.subheader("⏱ Estimated Time")

            st.write(
                question["estimated_time"]
            )

        if question.get("companies"):

            st.subheader("🏢 Frequently Asked In")

            companies = question["companies"]

            if isinstance(
                companies,
                list
            ):

                st.write(
                    ", ".join(companies)
                )

            else:

                st.write(companies)

        st.divider()

        c1, c2, c3 = st.columns(3)

        with c1:

            if st.button(
                "⬅ Previous",
                use_container_width=True
            ):

                if quiz.current_index > 0:

                    quiz.goto_question(
                        quiz.current_index - 1
                    )

                    st.session_state.answer_submitted = False

                    st.session_state.question_start_time = time.time()

                    st.rerun()

        with c2:

            if st.button(
                "Next Question ➜",
                use_container_width=True
            ):

                quiz.next_question()

                st.session_state.answer_submitted = False

                st.session_state.question_start_time = time.time()

                st.rerun()

        with c3:

            if st.button(
                "🏁 Finish Quiz",
                use_container_width=True
            ):

                while quiz.has_next():

                    quiz.next_question()

                st.rerun()