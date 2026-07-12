import streamlit as st


def show():

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success("✅ Resume Uploaded Successfully")

        st.markdown("---")

        st.subheader("Resume Analysis")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("ATS Score", "--")

        with c2:
            st.metric("Projects", "--")

        with c3:
            st.metric("Skills", "--")

        with c4:
            st.metric("Overall", "--")

        st.markdown("---")

        st.subheader("Suggestions")

        st.info("AI Resume Analysis will appear here.")

        st.markdown("---")

        st.subheader("Missing Skills")

        st.warning("Python")

        st.warning("SQL")

        st.warning("DBMS")

        st.warning("Operating System")

        st.warning("Computer Networks")

        st.markdown("---")

        st.subheader("Project Review")

        st.success("Projects will be analyzed here.")

        st.markdown("---")

        st.subheader("Interview Readiness")

        st.progress(0)

    else:

        st.info("Upload your resume to begin analysis.")