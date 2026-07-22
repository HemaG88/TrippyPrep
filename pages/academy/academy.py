import json
from pathlib import Path

import streamlit as st

from pages.academy import topic_browser

# -----------------------------------------------
# Data Path
# -----------------------------------------------

DATA_DIR = Path(__file__).parents[2] / "data" / "aptitude"


# -----------------------------------------------
# Load Aptitude Modules
# -----------------------------------------------

def load_topics():

    academy_file = DATA_DIR / "academy.json"

    with open(academy_file, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------------------------
# Aptitude Page
# -----------------------------------------------

def show():

    # ----------------------------
    # Session State
    # ----------------------------

    if "selected_topic" not in st.session_state:
        st.session_state.selected_topic = None

    if "selected_question_file" not in st.session_state:
        st.session_state.selected_question_file = None

    # ----------------------------
    # Open Topic Browser
    # ----------------------------

    if st.session_state.selected_topic is not None:
        topic_browser.show()
        return

    # ----------------------------
    # Header
    # ----------------------------

    st.title("🧮 Aptitude Academy")

    st.write("Choose a module to continue learning.")

    # ----------------------------
    # Back Button
    # ----------------------------

    if st.button("⬅ Back to Academy"):

        st.session_state.selected_academy = None
        st.session_state.selected_topic = None
        st.session_state.selected_question_file = None

        st.rerun()

    st.divider()

    # ----------------------------
    # Load Modules
    # ----------------------------

    topics = load_topics()

    cols = st.columns(2)

    for index, topic in enumerate(topics):

        with cols[index % 2]:

            if st.button(
                topic["name"],
                key=f"topic_{topic['id']}",
                use_container_width=True,
            ):

                st.session_state.selected_topic = topic
                st.rerun()
