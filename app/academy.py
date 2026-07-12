import streamlit as st
from services.academy_service import AcademyService
from services.topic_service import TopicService


def show():

    st.title("🎓 Placement Academy")

    stats = AcademyService.get_statistics()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Modules",
            stats["folders"]
        )

    with c2:
        st.metric(
            "Topics",
            stats["topics"]
        )

    with c3:
        st.metric(
            "Questions",
            stats["questions"]
        )

    st.markdown("---")

    st.subheader("Available Topics")

    topics = TopicService.get_all_topics()

    for topic in topics:

        st.write("📘", topic["name"])

    st.markdown("---")

    st.success("Complete every topic to become placement ready.")