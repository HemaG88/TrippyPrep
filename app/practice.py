import streamlit as st

from services.state_service import StateService
from services.topic_service import TopicService
from services.question_service import QuestionService


def show():

    topic_name = StateService.get_topic()

    if topic_name == "":
        st.warning("Select a topic first.")
        return

    topic = TopicService.get_topic(topic_name)

    if topic is None:
        st.error("Topic not found.")
        return

    path = f"data/aptitude/{topic['folder']}/{topic['file']}.json"

    try:
        questions = QuestionService.get_questions(path)

    except Exception:
        st.error(f"Questions file not found:\n{path}")
        return

    st.title(f"✍ Practice - {topic_name}")

    if len(questions) == 0:
        st.warning("No Questions Found")
        return

    if "question_index" not in st.session_state:
        st.session_state.question_index = 0

    index = st.session_state.question_index

    question = questions[index]

    st.progress((index + 1) / len(questions))

    st.subheader(f"Q{index + 1}. {question['question']}")

    answer = st.radio(
        "Choose your answer",
        question["options"],
        key=index
    )

    if st.button("Check Answer"):

        correct = question["options"][question["correct_option"] - 1]

        if answer == correct:
            st.success("✅ Correct")
        else:
            st.error(f"❌ Correct Answer: {correct}")

        st.info(question["explanation"])
        st.info(question["shortcut"])
        st.info(question["formula"])

    c1, c2 = st.columns(2)

    with c1:

        if st.button("⬅ Previous"):

            if index > 0:
                st.session_state.question_index -= 1
                st.rerun()

    with c2:

        if st.button("Next ➡"):

            if index < len(questions) - 1:
                st.session_state.question_index += 1
                st.rerun()