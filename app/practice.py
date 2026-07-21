import streamlit as st


def show():

    st.title("✍ Practice")

    st.caption(
        "Practice Questions by Difficulty"
    )

    st.divider()

    mode = st.selectbox(

        "Practice Mode",

        [

            "Easy",

            "Medium",

            "Hard",

            "Mixed",

        ],

    )

    count = st.slider(

        "Number of Questions",

        5,

        50,

        10,

        5,

    )

    st.divider()

    st.subheader("Practice Options")

    timed = st.checkbox("⏱ Timed Practice")

    explanation = st.checkbox(

        "📖 Show Explanation After Each Question",

        value=True,

    )

    shuffle = st.checkbox(

        "🔀 Shuffle Questions",

        value=True,

    )

    st.divider()

    st.success(

        f"Difficulty : {mode}"

    )

    st.write(

        f"Questions : {count}"

    )

    if timed:

        st.write("Mode : Timed")

    else:

        st.write("Mode : Normal")

    st.divider()

    st.button(

        "🚀 Start Practice",

        use_container_width=True,

    )