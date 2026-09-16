import streamlit as st

from components.auth import login_user
from pages.dashboard import dashboard


st.set_page_config(
    page_title="Sistem Master Material",
    page_icon="📦",
    layout="wide"
)


if "login" not in st.session_state:
    st.session_state.login = False


if st.session_state.login == False:

    login_user()


else:

    st.sidebar.title(
        "Sistem Master Material"
    )


    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Dashboard",
            "Form Permintaan Material",
            "Approval Workspace",
            "Dokumen Persetujuan",
            "Profile"
        ]
    )


    if menu=="Dashboard":
        dashboard()


    elif menu=="Form Permintaan Material":

        from pages.form_material import form_material
        form_material()


    elif menu=="Approval Workspace":

        from pages.approval import approval
        approval()


    elif menu=="Dokumen Persetujuan":

        from pages.document import document
        document()


    elif menu=="Profile":

        from pages.profile import profile
