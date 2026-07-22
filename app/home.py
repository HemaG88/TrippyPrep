import streamlit as st

from services.dashboard_service import DashboardService
from services.roadmap_service import RoadmapService


def show():

    data = DashboardService.get_dashboard_data()

    st.title("💀 TrippyPrep")
    st.caption("Your AI Placement Preparation Companion")

    st.divider()

    # ==========================================
    # Dashboard Summary
    # ==========================================

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

    # ==========================================
    # Quick Actions
    # ==========================================

    st.subheader("🚀 Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button(
            "🎓 Academy",
            use_container_width=True,
        )

    with c2:
        st.button(
            "📊 Dashboard",
            use_container_width=True,
        )

    with c3:
        st.button(
            "🤖 AI Mentor",
            use_container_width=True,
        )

    st.divider()

    # ==========================================
    # Recent Activity
    # ==========================================

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

    st.divider()

    # ==========================================
    # Placement Roadmap
    # ==========================================

    st.subheader("🗺 Placement Roadmap")

    roadmap = RoadmapService.get_roadmap()

    for step in roadmap:

        with st.expander(step["title"]):

            st.write(step["description"])