import streamlit as st

from services.stats_service import StatsService
from services.recommendation_service import RecommendationService
from services.roadmap_service import RoadmapService


def show():

    st.title("💀 TrippyPrep")

    st.subheader("AI Powered Placement Preparation Platform")

    st.markdown("---")

    # -----------------------------
    # Dashboard Statistics
    # -----------------------------

    stats = StatsService.get_dashboard_stats()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Tests Completed",
            stats["tests_completed"]
        )

    with c2:
        st.metric(
            "Questions Solved",
            stats["questions_solved"]
        )

    with c3:
        st.metric(
            "Average Accuracy",
            f"{stats['average_accuracy']}%"
        )

    with c4:
        st.metric(
            "Question Bank",
            stats["academy_questions"]
        )

    st.markdown("---")

    # -----------------------------
    # AI Recommendation
    # -----------------------------

    st.subheader("🎯 AI Recommendation")

    st.success(
        RecommendationService.get_recommendation()
    )

    st.markdown("---")

    # -----------------------------
    # Today's Roadmap
    # -----------------------------

    st.subheader("📅 Today's Roadmap")

    for task in RoadmapService.get_daily_plan():

        st.checkbox(task)

    st.markdown("---")

    # -----------------------------
    # Quick Access
    # -----------------------------

    st.subheader("🚀 Quick Access")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button(
            "📖 Learning",
            use_container_width=True
        )

    with col2:
        st.button(
            "✍ Practice",
            use_container_width=True
        )

    with col3:
        st.button(
            "🏢 Company Prep",
            use_container_width=True
        )

    st.markdown("---")

    # -----------------------------
    # Welcome
    # -----------------------------

    st.info(
        """
Welcome to **TrippyPrep** 🚀

Your AI-powered placement preparation platform.

✔ Learn Concepts

✔ Practice Questions

✔ Company-wise Preparation

✔ Mock Interviews

✔ Resume Analyzer

✔ Progress Tracking

Stay consistent. Small improvements every day lead to placement success.
"""
    )