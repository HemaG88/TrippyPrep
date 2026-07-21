import streamlit as st


def show():

    st.title("🤖 AI Mentor")

    st.caption(
        "Your Personal Placement Assistant"
    )

    st.divider()

    question = st.text_area(
        "Ask anything...",
        placeholder="Example: Explain Binary Search"
    )

    if st.button(
        "💬 Ask AI",
        use_container_width=True,
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            st.info(
                "AI integration coming soon..."
            )

    st.divider()

    st.subheader("Suggested Questions")

    suggestions = [

        "Explain Time Complexity",

        "Difference between Stack and Queue",

        "How to prepare for TCS?",

        "What are DBMS Normal Forms?",

        "Top HR Interview Questions"
    ]

    for item in suggestions:

        st.write(f"• {item}")