import streamlit as st


def show():

    st.title("📄 Resume Analyzer")

    st.caption(
        "Analyze your resume using AI"
    )

    st.divider()

    resume = st.file_uploader(

        "Upload Resume",

        type=["pdf", "docx"],

    )

    if resume is None:

        st.info(
            "Upload your resume to continue."
        )

        return

    st.success(
        f"Uploaded : {resume.name}"
    )

    st.divider()

    st.subheader("Analysis")

    st.progress(0)

    st.write("✔ Resume uploaded successfully")

    st.write("✔ Parsing resume")

    st.write("✔ Skills detection")

    st.write("✔ ATS score (Coming Soon)")

    st.write("✔ AI Suggestions (Coming Soon)")

    st.divider()

    st.button(

        "🤖 Analyze Resume",

        use_container_width=True,

    )s