from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="AI-FED",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {
            padding: 0;
            max-width: 100%;
        }
        iframe {
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

components.html(html, height=9000, scrolling=True)
