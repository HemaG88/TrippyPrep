import streamlit as st

from services.learning_service import LearningService


def show():

    if "selected_question_file" not in st.session_state:

        st.warning("Select a topic first.")

        return

    notes = LearningService.get_notes(
        st.session_state.selected_question_file
    )

    st.title("📖 Learning Mode")

    for i, note in enumerate(notes, start=1):

        with st.expander(f"Concept {i}"):

            st.subheader("Question")

            st.write(note["question"])

            if note["formula"]:

                st.subheader("Formula")

                st.code(note["formula"])

            if note["shortcut"]:

                st.subheader("Shortcut")

                st.success(note["shortcut"])

            if note["tip"]:

                st.subheader("Learning Tip")

                st.info(note["tip"])

            if note["explanation"]:

                st.subheader("Explanation")

                st.write(note["explanation"])
                st.divider()

c1, c2 = st.columns(2)

with c1:

    if st.button(
        "⬅ Back",
        use_container_width=True
    ):

        st.session_state.selected_question_file = None

        st.rerun()

with c2:

    if st.button(
        "🚀 Start Quiz",
        use_container_width=True
    ):

        st.session_state.learning_mode = False

        st.rerun()