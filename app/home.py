import streamlit as st

from services.dashboard_service import DashboardService


def show():

    data = DashboardService.get_dashboard_data()

    st.title("💀 TrippyPrep")

    st.caption("Your AI Placement Preparation Companion")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📝 Tests",
            data["tests_completed"]
        )

    with c2:
        st.metric(
            "⭐ XP",
            data["xp"]
        )

    with c3:
        st.metric(
            "🏆 Level",
            data["level"]
        )

    with c4:
        st.metric(
            "📚 Topics",
            data["completed_topics"]
        )

    st.divider()

    st.subheader("🚀 Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button(
            "🎓 Academy",
            use_container_width=True,
        ):
            st.session_state.selected_question_file = None

    with c2:
        if st.button(
            "📊 Dashboard",
            use_container_width=True,
        ):
            pass

    with c3:
        if st.button(
            "🤖 AI Mentor",
            use_container_width=True,
        ):
            pass

    st.divider()

    st.subheader("🕒 Recent Activity")

    if not data["recent"]:

        st.info("No recent activity.")

    else:

        for activity in data["recent"]:

            st.write(
                f"📘 {activity['topic']} • "
                f"{activity['score']}/{activity['total']} • "
                f"{activity['accuracy']}%"
            )