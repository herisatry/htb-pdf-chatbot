import streamlit as st
from app.auth import login_screen
from app.ui import run_chatbot_app

st.set_page_config(page_title="HTB Chatbot", page_icon=":robot_face:", layout="wide")

if not login_screen():
    st.stop()

run_chatbot_app()
