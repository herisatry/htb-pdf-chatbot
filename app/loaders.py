import os
import fitz
from langchain.text_splitter import CharacterTextSplitter

def extract_text_from_pdfs(folder_path):
    text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            doc = fitz.open(os.path.join(folder_path, filename))
            for page in doc:
                text += page.get_text()
    return text

def chunk_text(text, chunk_size=1000, chunk_overlap=100):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
