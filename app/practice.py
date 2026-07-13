import streamlit as st

from services.question_service import QuestionService
from services.progress_service import ProgressService
from services.report_service import ReportService
from services.streak_service import StreakService
from services.leaderboard_service import LeaderboardService


def show():

    st.title("✍ Practice")

    topic = st.selectbox(
        "Select Topic",
        [
            "aptitude/01_foundation/percentage.json",
            "aptitude/01_foundation/profit_loss.json",
            "aptitude/01_foundation/average.json",
            "aptitude/02_arithmetic/ages.json",
            "aptitude/02_arithmetic/time_and_work.json",
        ],
    )

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "current" not in st.session_state:
        st.session_state.current = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if "practice_started" not in st.session_state:
        st.session_state.practice_started = False

    # =====================================
    # Start Practice
    # =====================================

    if not st.session_state.practice_started:

        st.info("Click Start Practice to begin.")

        if st.button("🚀 Start Practice", use_container_width=True):

            st.session_state.questions = (
                QuestionService.get_random_questions(
                    topic,
                    10
                )
            )

            st.session_state.current = 0
            st.session_state.answers = {}
            st.session_state.practice_started = True

            st.rerun()

        return

    # =====================================
    # Question Screen
    # =====================================

    questions = st.session_state.questions

    if st.session_state.current < len(questions):

        q = questions[st.session_state.current]

        st.progress(
            (st.session_state.current + 1)
            / len(questions)
        )

        st.subheader(
            f"Question {st.session_state.current + 1} / {len(questions)}"
        )

        st.write(q["question"])

        answer = st.radio(
            "Choose Answer",
            q["options"],
            key=f"radio_{st.session_state.current}"
        )

        col1, col2 = st.columns(2)

        with col2:

            if st.button(
                "Next ➜",
                use_container_width=True
            ):

                st.session_state.answers[
                    st.session_state.current
                ] = answer

                st.session_state.current += 1

                st.rerun()

        return

    # =====================================
    # Result
    # =====================================

    result = QuestionService.check_answers(
        questions,
        st.session_state.answers
    )

    ProgressService.save_result(
        result["score"],
        result["total"],
        result["accuracy"]
    )

    StreakService.update_streak()

    LeaderboardService.save_result(
        result["score"],
        result["total"],
        result["accuracy"]
    )

    report = ReportService.generate_report(result)

    st.success("🎉 Practice Test Completed")

    c1, c2, c3, c4 = st.columns(4)

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
            "Wrong",
            len(result["wrong"])
        )

    with c4:
        st.metric(
            "Accuracy",
            f"{result['accuracy']}%"
        )

    st.markdown("---")

    st.subheader("📋 Test Summary")

    st.write(f"📅 Date : {report['date']}")
    st.write(f"🎯 Score : {report['score']}/{report['total']}")
    st.write(f"✅ Correct : {report['correct']}")
    st.write(f"❌ Wrong : {report['wrong']}")
    st.write(f"📈 Accuracy : {report['accuracy']}%")

    st.markdown("---")

    st.subheader("❌ Wrong Answers Review")

    if len(result["wrong"]) == 0:

        st.success(
            "Perfect Score! Excellent work 🎉"
        )

    else:

        for i, q in enumerate(result["wrong"], start=1):

            with st.expander(f"Question {i}"):

                st.write("### Question")
                st.write(q["question"])

                st.write("### Your Answer")
                st.error(q["your_answer"])

                st.write("### Correct Answer")
                st.success(q["correct_answer"])

                st.write("### Explanation")
                st.info(q["explanation"])

    st.markdown("---")

    if st.button(
        "🔄 Practice Again",
        use_container_width=True
    ):

        st.session_state.questions = []
        st.session_state.answers = {}
        st.session_state.current = 0
        st.session_state.practice_started = False

        st.rerun()