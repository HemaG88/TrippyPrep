import streamlit as st
from services.question_service import QuestionService
from services.topic_service import TopicService


def show():

    st.title("📚 Learning Center")

    topics = TopicService.get_all_topics()

    topic_names = [t["name"] for t in topics]

    selected = st.selectbox(
        "Choose Topic",
        topic_names
    )

    topic = next(
        t for t in topics
        if t["name"] == selected
    )

    if st.button("Open Lesson"):

        questions = QuestionService.get_questions(
            topic["path"]
        )

        if not questions:

            st.warning("No lesson available.")
            return

        q = questions[0]

        st.markdown("---")

        st.subheader(q["topic"])

        st.write("### 📘 Formula")
        st.success(q["formula"])

        st.write("### 💡 Shortcut")
        st.info(q["shortcut"])

        st.write("### 🎯 Learning Tip")
        st.warning(q["learning_tip"])

        st.write("### 📝 Example")

        st.write(q["question"])

        if "options" in q:

            for option in q["options"]:

                st.write(f"• {option}")

        st.write("### ✅ Correct Answer")

        st.success(q["correct_option"])

        st.write("### 📖 Explanation")

        st.write(q["explanation"])