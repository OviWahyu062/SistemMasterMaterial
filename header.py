
import streamlit as st

def header():
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/logo_danantara.png", width=120)
    with col2:
        st.image("assets/logo_bima.png", width=120)
