import streamlit as st

from services.dashboard_service import DashboardService


def show():

    data = DashboardService.get_dashboard_data()

    st.title("📊 Dashboard")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

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

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🎯 Best Accuracy",
            f"{data['best_accuracy']}%"
        )

    with c2:
        st.metric(
            "✅ Topics Completed",
            data["completed_topics"]
        )

    with c3:
        st.metric(
            "🔖 Bookmarks",
            data["bookmarks"]
        )

    st.divider()

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