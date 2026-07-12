import streamlit as st
from services.stats_service import StatsService


def show():

    st.title("📊 Dashboard")

    stats = StatsService.get_dashboard_stats()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Tests",
            stats["tests_completed"]
        )

    with c2:
        st.metric(
            "Solved",
            stats["questions_solved"]
        )

    with c3:
        st.metric(
            "Accuracy",
            f"{stats['average_accuracy']}%"
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "Best Accuracy",
            f"{stats['best_accuracy']}%"
        )

    with c5:
        st.metric(
            "Topics",
            stats["academy_topics"]
        )

    with c6:
        st.metric(
            "Question Bank",
            stats["academy_questions"]
        )

    st.markdown("---")

    st.subheader("Overall Progress")

    st.progress(
        min(stats["average_accuracy"] / 100, 1.0)
    )

    st.markdown("---")

    if stats["tests_completed"] == 0:

        st.info("No practice completed.")

    else:

        st.success("Keep practicing every day to improve your placement readiness.")