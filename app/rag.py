from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings()
    return FAISS.from_texts(chunks, embeddings)

def create_qa_chain(vectorstore):
    llm = Ollama(model="mistral")
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
