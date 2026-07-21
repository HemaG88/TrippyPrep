import streamlit as st

from services.learning_service import LearningService
from services.company_service import CompanyService
from services.topic_statistics_service import TopicStatisticsService


def show():

    if "selected_question_file" not in st.session_state:

        st.warning("Select a topic first.")
        return

    notes = LearningService.get_notes(
        st.session_state.selected_question_file
    )

    companies = CompanyService.get_companies_for_question(
        st.session_state.selected_question_file
    )

    stats = TopicStatisticsService.get_statistics(
        st.session_state.selected_question_file
    )

    st.title("📖 Learning Mode")

    # ==========================================
    # Topic Statistics
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Questions", stats["questions"])

    with c2:
        st.metric("Easy", stats["easy"])

    with c3:
        st.metric("Medium", stats["medium"])

    with c4:
        st.metric("Hard", stats["hard"])

    st.divider()

    # ==========================================
    # Companies
    # ==========================================

    if companies:

        st.subheader("🏢 Asked In Companies")
        st.write(" • ".join(companies))
        st.divider()

    # ==========================================
    # Notes
    # ==========================================

    for i, note in enumerate(notes, start=1):

        with st.expander(f"Concept {i}"):

            st.subheader("Question")
            st.write(note["question"])

            if note.get("formula"):
                st.subheader("📐 Formula")
                st.code(note["formula"])

            if note.get("shortcut"):
                st.subheader("⚡ Shortcut")
                st.success(note["shortcut"])

            if note.get("learning_tip"):
                st.subheader("💡 Learning Tip")
                st.info(note["learning_tip"])

            elif note.get("tip"):
                st.subheader("💡 Learning Tip")
                st.info(note["tip"])

            if note.get("explanation"):
                st.subheader("📖 Explanation")
                st.write(note["explanation"])

    st.divider()

    # ==========================================
    # Bottom Buttons
    # ==========================================

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "⬅ Back",
            use_container_width=True
        ):

            st.session_state.selected_question_file = None
            st.session_state.learning_mode = False

            st.rerun()

    with c2:

        if st.button(
            "🚀 Start Quiz",
            use_container_width=True
        ):

            st.session_state.learning_mode = False

            st.rerun()