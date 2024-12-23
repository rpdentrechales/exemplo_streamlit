import streamlit as st

# --- PAGE SETUP ---
page_1 = st.Page(
    "views/page_1.py",
    title="Sample Page 1",
    icon=":material/thumb_up:"
)

# --- PAGE SETUP ---
page_2 = st.Page(
    "views/page_2.py",
    title="Sample Page 2",
    icon=":material/home:",
    default=True,
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Pages": [page_1,page_2]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
