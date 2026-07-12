import streamlit as st
from services.stats_service import StatsService
from services.recommendation_service import RecommendationService


def show():

    st.title("💀 TrippyPrep")

    st.subheader("AI Powered Placement Preparation Platform")

    st.markdown("---")

    stats = StatsService.get_dashboard_stats()

    c1, c2, c3, c4 = st.columns(4)

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

    with c4:
        st.metric(
            "Question Bank",
            stats["academy_questions"]
        )

    st.markdown("---")

    st.subheader("🎯 AI Recommendation")

    st.success(
        RecommendationService.get_recommendation()
    )

    st.markdown("---")

    st.subheader("Quick Access")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("📖 Learning")

    with col2:
        st.button("✍ Practice")

    with col3:
        st.button("🏢 Company Prep")

    st.markdown("---")

    st.info("Welcome to TrippyPrep. Practice consistently and track your progress.")