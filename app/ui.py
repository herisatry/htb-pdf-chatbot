import os
import streamlit as st
from app.loaders import extract_text_from_pdfs, chunk_text
from app.rag import create_vectorstore, create_qa_chain

def load_knowledge(pdf_folder, chunk_size, chunk_overlap):
    text = extract_text_from_pdfs(pdf_folder)
    chunks = chunk_text(text, chunk_size, chunk_overlap)
    vectorstore = create_vectorstore(chunks)
    qa_chain = create_qa_chain(vectorstore)
    return vectorstore, qa_chain

def run_chatbot_app():
    with st.sidebar:
        if st.button("Logout"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.experimental_rerun()

        st.header("Settings")
        pdf_folder = st.text_input("PDF Folder Path", value="./pdfs")
        chunk_size = st.slider("Chunk Size", 500, 2000, 1000)
        chunk_overlap = st.slider("Chunk Overlap", 0, 500, 100)

        if st.button("Reload PDFs"):
            vectorstore, qa_chain = load_knowledge(pdf_folder, chunk_size, chunk_overlap)
            st.session_state.vectorstore = vectorstore
            st.session_state.qa_chain = qa_chain
            st.session_state.messages = []

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if pdf_folder and "vectorstore" not in st.session_state:
        if os.path.exists(pdf_folder):
            with st.spinner("Loading PDFs..."):
                vectorstore, qa_chain = load_knowledge(pdf_folder, chunk_size, chunk_overlap)
                st.session_state.vectorstore = vectorstore
                st.session_state.qa_chain = qa_chain
            st.success("PDFs loaded!")

    st.title("HackTheBox Walkthrough Chatbot")

    query = st.chat_input("Ask something about the PDFs...")

    if query and "qa_chain" in st.session_state:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.spinner("Thinking..."):
            answer = st.session_state.qa_chain.run(query)
        st.session_state.messages.append({"role": "assistant", "content": answer})

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])
