col1, col2 = st.columns([4, 1])

with col1:

    if st.button(
        topic["name"],
        use_container_width=True,
        key=f"quiz_{topic['file']}"
    ):

        st.session_state.selected_question_file = topic["file"]
        st.session_state.learning_mode = False

        st.rerun()

with col2:

    if st.button(
        "📖",
        key=f"learn_{topic['file']}"
    ):

        st.session_state.selected_question_file = topic["file"]
        st.session_state.learning_mode = True

        st.rerun()