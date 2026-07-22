import streamlit as st

from services.progress_service import ProgressService
from services.xp_tracker_service import XPTrackerService


def show():

    progress = ProgressService.load_progress()

    xp = XPTrackerService.load()

    st.title("👤 Profile")

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "⭐ XP",
            xp["xp"]
        )

    with c2:

        st.metric(
            "🏆 Level",
            xp["level"]
        )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "📝 Tests Completed",
            progress["tests_completed"]
        )

    with c2:

        st.metric(
            "🎯 Best Accuracy",
            f"{progress['best_accuracy']}%"
        )

    st.divider()

    st.metric(
        "📚 Questions Solved",
        progress["total_questions"]
    )

    st.metric(
        "✅ Correct Answers",
        progress["total_score"]
    )

    st.divider()

    st.success("Keep learning every day 🚀")