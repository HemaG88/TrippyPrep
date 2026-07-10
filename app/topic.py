import streamlit as st

from services.state_service import StateService
from services.topic_service import TopicService


def show():

    academy = StateService.get_academy()

    if academy == "":
        st.warning("Select an Academy first.")
        return

    topics = TopicService.get_topics_by_folder(academy)

    st.title("📚 Topics")

    if len(topics) == 0:
        st.warning("No topics found.")
        return

    for topic in topics:

        col1, col2 = st.columns([5, 1])

        with col1:

            if st.button(
                f"📘 {topic['name']}",
                key=topic["id"],
                use_container_width=True,
            ):

                StateService.save_topic(topic["name"])

                st.success(f"Selected : {topic['name']}")

        with col2:

            st.write("➡️")

    st.divider()

    selected = StateService.get_topic()

    if selected != "":

        st.success(f"Current Topic : {selected}")