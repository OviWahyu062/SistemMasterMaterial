
import streamlit as st

def form_material():
    st.header("Form Permintaan Material")
    st.text_input("Nama Material *")
    st.text_input("URL Dokumen / Link Manual *")
    st.file_uploader("Upload Gambar (Opsional)")
