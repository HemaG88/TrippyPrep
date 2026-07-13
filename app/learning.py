import streamlit as st

from services.search_service import SearchService
from services.question_service import QuestionService
from services.academy_progress_service import AcademyProgressService


def show():

    st.title("📚 Learning Center")

    st.write("Search any aptitude topic and learn it step by step.")

    st.markdown("---")

    keyword = st.text_input(
        "🔍 Search Topic"
    )

    if keyword.strip() == "":

        st.info("Start typing a topic name (Example: Percentage, Profit, Average...)")

        return

    topics = SearchService.search_topics(keyword)

    if len(topics) == 0:

        st.warning("No matching topics found.")

        return

    names = [
        topic["name"]
        for topic in topics
    ]

    selected = st.selectbox(
        "Select Topic",
        names
    )

    topic = next(
        t
        for t in topics
        if t["name"] == selected
    )

    st.markdown("---")

    if AcademyProgressService.is_completed(topic["path"]):

        st.success("✅ Topic Already Completed")

    else:

        st.info("📖 Topic Not Completed")

    if st.button(
        "📖 Open Lesson",
        use_container_width=True
    ):

        questions = QuestionService.get_questions(
            topic["path"]
        )

        if len(questions) == 0:

            st.error("No lesson available.")

            return

        q = questions[0]

        st.markdown("---")

        st.header(q["topic"])

        st.caption(
            f"Difficulty : {q['difficulty']}"
        )

        st.markdown("---")

        st.subheader("📘 Formula")

        st.success(
            q["formula"]
        )

        st.subheader("⚡ Shortcut")

        st.info(
            q["shortcut"]
        )

        st.subheader("💡 Learning Tip")

        st.warning(
            q["learning_tip"]
        )

        st.markdown("---")

        st.subheader("📝 Example Question")

        st.write(
            q["question"]
        )

        for option in q["options"]:

            st.write(f"• {option}")

        st.markdown("---")

        st.subheader("✅ Correct Answer")

        st.success(
            q["correct_option"]
        )

        st.subheader("📖 Explanation")

        st.write(
            q["explanation"]
        )

        st.markdown("---")

        st.subheader("🏢 Asked In Companies")

        if "companies" in q and len(q["companies"]) > 0:

            for company in q["companies"]:

                st.write(f"✔ {company}")

        else:

            st.info("Company data not available.")

        st.markdown("---")

        if st.button(
            "✅ Mark Topic Completed",
            use_container_width=True
        ):

            AcademyProgressService.mark_completed(
                topic["path"]
            )

            st.success(
                "Topic marked as completed."
            )

            st.rerun()

        st.markdown("---")

        st.success(
            "🎉 Lesson Completed Successfully!"
        )