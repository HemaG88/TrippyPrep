import streamlit as st
from services.question_service import QuestionService
from services.search_service import SearchService


def show():

    st.title("📚 Learning Center")

    keyword = st.text_input(
        "🔍 Search Topic"
    )

    if keyword == "":

        st.info("Search any topic.")

        return

    topics = SearchService.search_topics(keyword)

    if len(topics) == 0:

        st.warning("No topic found.")

        return

    names = [t["name"] for t in topics]

    selected = st.selectbox(
        "Results",
        names
    )

    topic = next(
        t for t in topics
        if t["name"] == selected
    )

    if st.button("Open Lesson"):

        questions = QuestionService.get_questions(
            topic["path"]
        )

        q = questions[0]

        st.markdown("---")

        st.subheader(q["topic"])

        st.success(q["formula"])

        st.info(q["shortcut"])

        st.warning(q["learning_tip"])

        st.markdown("---")

        st.write(q["question"])

        for option in q["options"]:

            st.write(f"• {option}")

        st.success(q["correct_option"])

        st.write(q["explanation"])