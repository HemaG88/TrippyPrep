import streamlit as st

from services.academy_service import AcademyService
from services.topic_progress_service import TopicProgressService


def show():

    if "selected_topic" not in st.session_state:
        st.session_state.selected_topic = None

    if st.session_state.selected_topic is not None:
        from pages.academy import topic_browser
        topic_browser.show(
            st.session_state.selected_topic["folder"]
        )
        return

    st.title("🧮 Aptitude Academy")
    st.caption("Master Aptitude for Placements")

    # ==========================================
    # Search
    # ==========================================

    search = st.text_input(
        "🔍 Search Topic"
    )

    if search:

        topics = AcademyService.search_topics(
            search
        )

    else:

        topics = AcademyService.get_aptitude_topics()

    # ==========================================
    # Statistics
    # ==========================================

    total_topics = len(topics)

    completed = sum(
        TopicProgressService.is_completed(
            topic["file"]
        )
        for topic in topics
    )

    percent = round(
        (completed / total_topics) * 100,
        2
    ) if total_topics else 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Topics",
            total_topics
        )

    with col2:
        st.metric(
            "Completed",
            completed
        )

    with col3:
        st.metric(
            "Progress",
            f"{percent}%"
        )

    st.progress(percent / 100)

    st.divider()

    # ==========================================
    # Topic List
    # ==========================================

    folders = {}

    for topic in topics:

        folders.setdefault(
            topic["folder"],
            []
        ).append(topic)

    for folder, values in folders.items():

        with st.expander(
            f"📂 {folder.replace('_', ' ').title()} ({len(values)} Topics)",
            expanded=False,
        ):

            for topic in values:

                if st.button(
                    topic["name"],
                    key=topic["id"],
                    use_container_width=True,
                ):

                    st.session_state.selected_topic = topic

                    st.rerun()