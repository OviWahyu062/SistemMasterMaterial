
import streamlit as st

def login_user():
    st.subheader("Login Sistem Master Material")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state.login = True
        st.success("Login berhasil")
