import streamlit as st

from services.stats_service import StatsService
from services.analytics_service import AnalyticsService
from services.achievement_service import AchievementService
from services.streak_service import StreakService
from services.leaderboard_service import LeaderboardService
from services.academy_progress_service import AcademyProgressService


def show():

    st.title("📊 TrippyPrep Dashboard")

    # ===============================
    # Safe Loading
    # ===============================

    try:
        stats = StatsService.get_dashboard_stats()
    except Exception:
        stats = {
            "academy_questions": 0,
            "best_accuracy": 0
        }

    try:
        analytics = AnalyticsService.get_summary()
    except Exception:
        analytics = {
            "tests": 0,
            "questions": 0,
            "correct": 0,
            "accuracy": 0,
            "level": "Beginner"
        }

    try:
        streak = StreakService.get_streak()
    except Exception:
        streak = 0

    try:
        completed_topics = AcademyProgressService.completed_count()
    except Exception:
        completed_topics = 0

    # ===============================
    # Top Cards
    # ===============================

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("📝 Tests", analytics["tests"])
    c2.metric("📚 Questions", analytics["questions"])
    c3.metric("🎯 Accuracy", f"{analytics['accuracy']}%")
    c4.metric("🔥 Streak", streak)
    c5.metric("✅ Topics", completed_topics)

    st.divider()

    # ===============================
    # Statistics
    # ===============================

    st.subheader("📈 Overall Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**Tests Completed :** {analytics['tests']}")
        st.write(f"**Questions Solved :** {analytics['questions']}")
        st.write(f"**Correct Answers :** {analytics['correct']}")
        st.write(f"**Current Level :** {analytics['level']}")

    with col2:

        st.write(f"**Best Accuracy :** {stats['best_accuracy']}%")
        st.write(f"**Question Bank :** {stats['academy_questions']}")
        st.write(f"**Learning Progress :** {completed_topics} Topics")
        st.write(f"**Current Streak :** {streak} Day(s)")

    st.divider()

    # ===============================
    # Progress
    # ===============================

    st.subheader("📊 Accuracy Progress")

    accuracy = analytics["accuracy"]

    st.progress(min(accuracy / 100, 1.0))

    st.write(f"Current Accuracy : **{accuracy}%**")

    st.divider()

    # ===============================
    # Achievements
    # ===============================

    st.subheader("🏆 Achievements")

    try:
        badges = AchievementService.get_badges()
    except Exception:
        badges = []

    if len(badges) == 0:

        st.info("No achievements unlocked yet.")

    else:

        cols = st.columns(3)

        for i, badge in enumerate(badges):

            cols[i % 3].success(badge)

    st.divider()

    # ===============================
    # Leaderboard
    # ===============================

    st.subheader("🥇 Best Practice Results")

    try:
        records = LeaderboardService.load()
    except Exception:
        records = []

    if len(records) == 0:

        st.info("No practice history available.")

    else:

        for i, record in enumerate(records, start=1):

            st.write(
                f"**{i}.** "
                f"Score **{record['score']}/{record['total']}** "
                f"| Accuracy **{record['accuracy']}%** "
                f"| {record['date']}"
            )

    st.divider()

    # ===============================
    # Performance Message
    # ===============================

    st.subheader("💡 Performance")

    if accuracy >= 90:

        st.success("🏆 Excellent! You're placement ready.")
        st.balloons()

    elif accuracy >= 75:

        st.success("🚀 Great Progress! Keep going.")

    elif accuracy >= 50:

        st.warning("📚 Good effort. Practice more to improve.")

    else:

        st.error("⚡ Start with the Academy and Practice sections.")

    st.divider()

    st.caption("TrippyPrep • AI Powered Placement Preparation Platform")