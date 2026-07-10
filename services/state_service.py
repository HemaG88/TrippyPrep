import streamlit as st


class StateService:

    @staticmethod
    def save_academy(folder):
        st.session_state["academy"] = folder

    @staticmethod
    def get_academy():
        return st.session_state.get("academy", "")

    @staticmethod
    def save_topic(topic):
        st.session_state["topic"] = topic

    @staticmethod
    def get_topic():
        return st.session_state.get("topic", "")

    @staticmethod
    def correct():
        st.session_state["correct"] = (
            st.session_state.get("correct", 0) + 1
        )

    @staticmethod
    def wrong():
        st.session_state["wrong"] = (
            st.session_state.get("wrong", 0) + 1
        )

    @staticmethod
    def reset():
        st.session_state["correct"] = 0
        st.session_state["wrong"] = 0