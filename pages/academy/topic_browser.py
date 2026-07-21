import json
from pathlib import Path

import streamlit as st

from services.topic_progress_service import TopicProgressService

DATA_DIR = Path("data/aptitude")


def show(folder_name):

    folder = DATA_DIR / folder_name
    topics_file = DATA_DIR / "aptitude_topics.json"

    if not topics_file.exists():
        st.error("❌ aptitude_topics.json not found.")
        return

    with open(topics_file, "r", encoding="utf-8") as f:
        topics = json.load(f)

    folder_topics = [
        t for t in topics
        if t["folder"] == folder_name
    ]

    st.title("📚 Topic Browser")
    st.subheader(folder_name.replace("_", " ").title())
    st.caption(f"{len(folder_topics)} Topics Available")

    st.divider()

    search = st.text_input(
        "🔍 Search Topic",
        placeholder="Search topic..."
    )

    col1, col2 = st.columns(2)

    with col1:
        show_completed = st.checkbox("Completed Only")

    with col2:
        show_pending = st.checkbox("Pending Only")

    if search:
        folder_topics = [
            t for t in folder_topics
            if search.lower() in t["name"].lower()
        ]

    if show_completed:
        folder_topics = [
            t for t in folder_topics
            if TopicProgressService.is_completed(t["file"])
        ]

    if show_pending:
        folder_topics = [
            t for t in folder_topics
            if not TopicProgressService.is_completed(t["file"])
        ]

    sort_by = st.selectbox(
        "Sort By",
        [
            "A-Z",
            "Completed First",
            "Pending First",
        ],
    )

    if sort_by == "A-Z":

        folder_topics.sort(
            key=lambda x: x["name"]
        )

    elif sort_by == "Completed First":

        folder_topics.sort(
            key=lambda x: not TopicProgressService.is_completed(
                x["file"]
            )
        )

    else:

        folder_topics.sort(
            key=lambda x: TopicProgressService.is_completed(
                x["file"]
            )
        )

    completed_topics = sum(
        TopicProgressService.is_completed(t["file"])
        for t in folder_topics
    )

    progress = (
        completed_topics / len(folder_topics)
        if folder_topics else 0
    )

    st.progress(progress)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Completed",
            completed_topics
        )

    with col2:
        st.metric(
            "Remaining",
            len(folder_topics) - completed_topics
        )

    st.caption(
        f"{completed_topics}/{len(folder_topics)} Topics Completed"
    )

    st.divider()

    if not folder_topics:
        st.info("No topics found.")
        return

    for topic in folder_topics:

        completed = TopicProgressService.is_completed(
            topic["file"]
        )

        title = (
            f"✅ {topic['name']}"
            if completed
            else f"📘 {topic['name']}"
        )

        col1, col2 = st.columns([7, 2])

        with col1:

            if st.button(
                title,
                key=f"quiz_{topic['id']}",
                use_container_width=True,
            ):

                st.session_state.selected_question_file = str(
                    folder / f"{topic['file']}.json"
                )

                st.session_state.learning_mode = False
                st.rerun()

        with col2:

            if st.button(
                "📖 Learn",
                key=f"learn_{topic['id']}",
                use_container_width=True,
            ):

                st.session_state.selected_question_file = str(
                    folder / f"{topic['file']}.json"
                )

                st.session_state.learning_mode = True
                st.rerun()

    st.divider()

    if st.button(
        "⬅ Back",
        use_container_width=True,
    ):

        st.session_state.selected_topic = None
        st.session_state.selected_question_file = None
        st.session_state.learning_mode = False

        st.rerun()