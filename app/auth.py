import streamlit as st
import os

def authenticate(username, password):
    return username == os.getenv("APP_USERNAME", "admin") and password == os.getenv("APP_PASSWORD", "admin")

def login_screen():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("Login Required")
        with st.form("login_form", clear_on_submit=True):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
        if submitted and authenticate(username, password):
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            st.experimental_rerun()
        elif submitted:
            st.error("Invalid username or password.")
    return st.session_state.authenticated
