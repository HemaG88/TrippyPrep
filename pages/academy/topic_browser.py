import streamlit as st
from pathlib import Path

from pages.academy import quiz

DATA_DIR = Path(__file__).parents[2] / "data" / "aptitude"


def show():

    # -----------------------------
    # Session State
    # -----------------------------

    if "selected_question_file" not in st.session_state:
        st.session_state.selected_question_file = None

    # -----------------------------
    # Open Quiz
    # -----------------------------

    if st.session_state.selected_question_file is not None:
        quiz.show()
        return

    # -----------------------------
    # Validate Module
    # -----------------------------

    if "selected_topic" not in st.session_state:
        st.error("No module selected.")
        return

    topic = st.session_state.selected_topic

    folder = DATA_DIR / topic["folder"]

    st.title(f"📚 {topic['name']}")

    if st.button("⬅ Back"):

        st.session_state.selected_topic = None
        st.rerun()

    st.divider()

    json_files = sorted(folder.glob("*.json"))

    cols = st.columns(2)

    for index, file in enumerate(json_files):

        with cols[index % 2]:

            topic_name = file.stem.replace("_", " ").title()

            if st.button(
                topic_name,
                key=file.stem,
                use_container_width=True,
            ):

                st.session_state.selected_question_file = str(file)
                st.rerun()