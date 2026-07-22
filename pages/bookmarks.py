import streamlit as st

from services.bookmark_service import BookmarkService


def show():

    st.title("🔖 Bookmarks")

    bookmarks = BookmarkService.load()

    if not bookmarks:

        st.info("No bookmarked questions.")

        return

    for question in bookmarks:

        with st.expander(question["question"]):

            st.write("### Options")

            for option in question["options"]:

                st.write(f"• {option}")

            st.divider()

            st.success(
                f"Correct Answer : Option {question['correct_option']}"
            )

            st.write(question["explanation"])

            if st.button(
                "🗑 Remove Bookmark",
                key=question["id"],
                use_container_width=True,
            ):

                BookmarkService.remove(
                    question["id"]
                )

                st.rerun()