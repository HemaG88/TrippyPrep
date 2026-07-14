import streamlit as st

from services.xp_service import XPService
from services.badge_service import BadgeService
from services.result_analysis_service import ResultAnalysisService


def show():

    if "quiz_engine" not in st.session_state:

        st.warning("No quiz completed.")
        return

    quiz = st.session_state.quiz_engine

    report = ResultAnalysisService.analyze(quiz)

    xp = XPService.calculate(
        report["score"],
        report["total"]
    )

    level = XPService.level(xp)

    badges = BadgeService.get_badges(
        report["score"],
        report["total"]
    )

    st.title("🏆 Quiz Result")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Score",
        f"{report['score']}/{report['total']}"
    )

    c2.metric(
        "Accuracy",
        f"{report['accuracy']}%"
    )

    c3.metric(
        "XP Earned",
        xp
    )

    c4.metric(
        "Level",
        level
    )

    st.divider()

    st.subheader("Performance")

    st.progress(report["accuracy"] / 100)

    st.write(f"Correct : {report['correct']}")

    st.write(f"Wrong : {report['wrong']}")

    st.write(f"Answered : {report['answered']}")

    st.write(f"Marked Review : {report['review']}")

    st.divider()

    st.subheader("Achievements")

    if badges:

        cols = st.columns(len(badges))

        for i, badge in enumerate(badges):

            cols[i].success(badge)

    else:

        st.info("No badges unlocked.")

    st.divider()

    st.subheader("Recommendation")

    if report["accuracy"] >= 90:

        st.success(
            "Excellent! You're placement ready."
        )

    elif report["accuracy"] >= 75:

        st.success(
            "Very Good. Continue practicing."
        )

    elif report["accuracy"] >= 50:

        st.warning(
            "Need more practice."
        )

    else:

        st.error(
            "Go back to Academy and strengthen fundamentals."
        )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🔄 Retry Quiz",
            use_container_width=True
        ):

            del st.session_state.quiz_engine

            st.session_state.quiz_completed = False
            st.session_state.answer_submitted = False
            st.session_state.last_answer_correct = False

            st.rerun()

    with c2:

        if st.button(
            "⬅ Back To Topics",
            use_container_width=True
        ):

            del st.session_state.quiz_engine

st.session_state.quiz_completed = False

st.session_state.selected_question_file = None

st.session_state.answer_submitted = False

st.session_state.last_answer_correct = False

st.rerun()