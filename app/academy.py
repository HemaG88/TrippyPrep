import json
from pathlib import Path

import streamlit as st

# Path to data folder
DATA_DIR = Path(__file__).parent.parent / "data"


def load_academies():
    """Load the main academy list."""

    academy_file = DATA_DIR / "academy.json"

    with open(academy_file, "r", encoding="utf-8") as file:
        return json.load(file)


def show():
    """Academy Screen"""

    # -----------------------------
    # Session State Initialization
    # -----------------------------
    if "selected_academy" not in st.session_state:
        st.session_state.selected_academy = None

    if "selected_topic" not in st.session_state:
        st.session_state.selected_topic = None

    # -----------------------------
    # Open Aptitude Page
    # -----------------------------
    if st.session_state.selected_academy == "aptitude":

        from pages.academy import aptitude

        aptitude.show()
        return

    # -----------------------------
    # Academy Home
    # -----------------------------
    st.title("🎓 Academy")
    st.write("Choose an academy to begin learning.")

    academies = load_academies()

    cols = st.columns(2)

    for index, academy in enumerate(academies):

        with cols[index % 2]:

            if st.button(
                academy["name"],
                key=f"academy_{academy['id']}",
                use_container_width=True,
            ):

                st.session_state.selected_academy = academy["folder"]
                st.rerun()