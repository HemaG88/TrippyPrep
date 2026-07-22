import streamlit as st

from services.dashboard_service import DashboardService
from services.recommendation_service import RecommendationService
from services.statistics_service import StatisticsService


def show():

    data = DashboardService.get_dashboard_data()
    stats = StatisticsService.get_statistics()

    st.title("📊 Dashboard")

    st.divider()

    # ==========================================
    # Top Metrics
    # ==========================================

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            "📝 Tests",
            data["tests_completed"]
        )

    with c2:
        st.metric(
            "📚 Questions",
            data["questions_solved"]
        )

    with c3:
        st.metric(
            "⭐ XP",
            data["xp"]
        )

    with c4:
        st.metric(
            "🏆 Level",
            data["level"]
        )

    with c5:
        st.metric(
            "🔥 Streak",
            data["streak"]
        )

    st.divider()

    # ==========================================
    # Achievements
    # ==========================================

    st.subheader("🏅 Achievements")

    if data["level"] >= 5:
        st.success("🏆 Level 5 Reached")

    if data["completed_topics"] >= 10:
        st.success("📚 Completed 10 Topics")

    if data["streak"] >= 7:
        st.success("🔥 7-Day Learning Streak")

    if data["tests_completed"] >= 25:
        st.success("🎯 Completed 25 Tests")

    st.divider()

    # ==========================================
    # AI Recommendations
    # ==========================================

    st.subheader("💡 AI Recommendations")

    recommendations = RecommendationService.get_recommendations()

    for item in recommendations:
        st.success(item)

    st.divider()

    # ==========================================
    # Recent Activity
    # ==========================================

    st.subheader("🕒 Recent Activity")

    if not data["recent"]:

        st.info("No activity yet.")

    else:

        for activity in data["recent"]:

            st.write(
                f"📘 {activity['topic']} | "
                f"{activity['score']}/{activity['total']} | "
                f"{activity['accuracy']}%"
            )

    st.divider()

    # ==========================================
    # Overall Statistics
    # ==========================================

    st.subheader("📈 Overall Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🔖 Bookmarks",
            stats["bookmarks"]
        )

    with c2:
        st.metric(
            "🚩 Reports",
            stats["reports"]
        )

    with c3:
        st.metric(
            "🔥 Streak",
            stats["streak"]
        )

    with c4:
        st.metric(
            "🎯 Best Accuracy",
            f"{stats['best_accuracy']}%"
        )