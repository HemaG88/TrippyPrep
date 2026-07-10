import streamlit as st

from services.state_service import StateService
from services.topic_service import TopicService
from services.notes_loader import NotesLoader


def show():

    topic_name = StateService.get_topic()

    if topic_name == "":
        st.warning("Select a topic first.")
        return

    topic = TopicService.get_topic(topic_name)

    if topic is None:
        st.error("Topic not found.")
        return

    path = f"notes/aptitude/{topic['folder']}/{topic['file']}.md"

    st.title(f"📖 {topic_name}")

    try:
        notes = NotesLoader.load(path)
        st.markdown(notes)

    except Exception:
        st.error(f"Notes not found:\n{path}")