import time
import streamlit as st

from services.json_loader import JSONLoader
from services.quiz_engine import QuizEngine
from services.bookmark_service import BookmarkService
from services.report_service import ReportService
from services.xp_tracker_service import XPTrackerService
from services.result_analysis_service import ResultAnalysisService


def show():

    if "selected_question_file" not in st.session_state:
        st.error("No topic selected.")
        return

    if (
        "quiz_engine" not in st.session_state
        or st.session_state.quiz_engine is None
    ):

        questions = JSONLoader.load(
            st.session_state.selected_question_file
        )

        st.session_state.quiz_engine = QuizEngine(
            questions
        )

    if "answer_submitted" not in st.session_state:
        st.session_state.answer_submitted = False

    if "last_answer_correct" not in st.session_state:
        st.session_state.last_answer_correct = False

    if "question_start_time" not in st.session_state:
        st.session_state.question_start_time = time.time()

    quiz = st.session_state.quiz_engine

    # ======================================================
    # Quiz Finished
    # ======================================================

    if not quiz.has_next():

        st.session_state.quiz_result = (
            ResultAnalysisService.analyze(quiz)
        )

        st.session_state.quiz_engine = None

        st.rerun()

    # ======================================================
    # Sidebar
    # ======================================================

    st.sidebar.title("📋 Question Palette")

    xp = XPTrackerService.load()

    st.sidebar.metric(
        "⭐ XP",
        xp["xp"]
    )

    st.sidebar.metric(
        "🏆 Level",
        xp["level"]
    )

    st.sidebar.divider()

    st.sidebar.metric(
        "✅ Score",
        quiz.get_score()
    )

    answered = 0

    for i in range(
        quiz.total_questions()
    ):

        if quiz.is_answered(i):
            answered += 1

    accuracy = 0

    if answered > 0:

        accuracy = round(
            quiz.get_score() / answered * 100,
            1
        )

    st.sidebar.metric(
        "🎯 Accuracy",
        f"{accuracy}%"
    )

    st.sidebar.divider()

    for i in range(
        quiz.total_questions()
    ):

        label = f"Q{i+1}"

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

    # ======================================================
    # Current Question
    # ======================================================

    question = quiz.current_question()

    st.title(
        f"Question {quiz.current_number()} / {quiz.total_questions()}"
    )

    st.progress(
        quiz.current_number() /
        quiz.total_questions()
    )

    elapsed = int(
        time.time()
        - st.session_state.question_start_time
    )

    st.info(
        f"⏱ {elapsed//60:02d}:{elapsed%60:02d}"
    )

    st.write("## " + question["question"])

    answer = st.radio(
        "Choose your answer",
        question["options"],
        index=None,
        key=f"answer_{quiz.current_number()}",
        disabled=st.session_state.answer_submitted,
    )

    # ======================================================
    # Action Buttons
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "🟡 Mark Review",
            use_container_width=True
        ):

            quiz.mark_review()

            st.rerun()

    with c2:

        if quiz.is_review(
            quiz.current_index
        ):

            if st.button(
                "❌ Remove",
                use_container_width=True
            ):

                quiz.unmark_review()

                st.rerun()

    with c3:

        if st.button(
            "⭐ Bookmark",
            use_container_width=True
        ):

            BookmarkService.add(
    question
)

            st.success("Bookmarked")

    with c4:

        if st.button(
            "🚩 Report",
            use_container_width=True
        ):

            ReportService.report(question)

            st.success("Reported")

    st.divider()

    # ======================================================
    # Submit
    # ======================================================

    if (
        not st.session_state.answer_submitted
        and st.button(
            "Submit",
            use_container_width=True
        )
    ):

        if answer is None:

            st.warning(
                "Please choose an answer."
            )

            st.stop()

        selected = (
            question["options"].index(answer)
            + 1
        )

        correct = quiz.check_answer(
            selected
        )

        if correct:
            XPTrackerService.add_xp(10)

        st.session_state.last_answer_correct = correct

        st.session_state.answer_submitted = True

        st.rerun()
            # ======================================================
    # Review Section
    # ======================================================

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

            st.subheader(
                "🏢 Frequently Asked In"
            )

            companies = question["companies"]

            if isinstance(companies, list):

                st.write(
                    ", ".join(companies)
                )

            else:

                st.write(companies)

        st.divider()

        c1, c2, c3 = st.columns(3)

        # =======================================
        # Previous
        # =======================================

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

        # =======================================
        # Next
        # =======================================

        with c2:

            if st.button(
                "Next ➜",
                use_container_width=True
            ):

                quiz.next_question()

                st.session_state.answer_submitted = False

                st.session_state.question_start_time = time.time()

                st.rerun()

        # =======================================
        # Finish Quiz
        # =======================================

        with c3:

            if st.button(
                "🏁 Finish Quiz",
                use_container_width=True
            ):

                st.session_state.quiz_result = (
                    ResultAnalysisService.analyze(
                        quiz
                    )
                )

                st.session_state.quiz_engine = None

                st.session_state.answer_submitted = False

                st.session_state.last_answer_correct = False

                st.rerun()

    # ======================================================
    # Bottom Progress
    # ======================================================

    st.divider()

    answered = quiz.answered_count()

    review = quiz.review_count()

    remaining = quiz.remaining_count()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Answered",
            answered
        )

    with c2:

        st.metric(
            "Review",
            review
        )

    with c3:

        st.metric(
            "Remaining",
            remaining
        )

    progress = 0

    if quiz.total_questions() > 0:

        progress = answered / quiz.total_questions()

    st.progress(progress)

    st.caption(
        f"{answered} / {quiz.total_questions()} Questions Answered"
    )