# 🛡️ HackTheBox Walkthrough PDF Chatbot (Modular RAG App)

This project is a **modular, fully local Retrieval-Augmented Generation (RAG) chatbot** built for security professionals and CTF players who collect **PDF-based walkthroughs** (e.g., from HackTheBox).  
It allows you to query your own documents using a private AI assistant — no internet needed.

...

# 🛡️ HackTheBox PDF Chatbot — Modular RAG App

A fully local, private, and modular Retrieval-Augmented Generation (RAG) chatbot for querying your HackTheBox walkthrough PDFs.  
Runs on your machine using Ollama + Streamlit + LangChain + FAISS.

---

## ✅ Features

- Chat with multiple HackTheBox PDF walkthroughs
- Streamlit-based dark themed Web UI
- Powered by local Mistral LLM via Ollama
- Fast semantic search using FAISS
- Reload PDFs manually via UI
- Simple login/logout (credentials via env)
- Dockerized and modularized for easy deployment and development
- GitHub push automation script included

---

## 📁 Project Structure

```
htb_pdf_chatbot/
├── main.py                 # Streamlit entrypoint
├── app/
│   ├── __init__.py
│   ├── auth.py             # Login logic
│   ├── loaders.py          # PDF extraction + chunking
│   ├── rag.py              # Embeddings + vectorstore + QA chain
│   └── ui.py               # UI logic and session state
├── .streamlit/config.toml # Dark mode UI theme
├── start.sh               # Starts Ollama + Docker Compose
├── push.sh                # Git push automation
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── pdfs/                  # Your HTB walkthrough PDFs
```

---

## 🚀 How to Run

### 1. Requirements

- [Install Ollama](https://ollama.com) and run `ollama pull mistral`
- Docker + Docker Compose installed

---

### 2. Start the App Locally

```bash
./start.sh
```

Then visit: **http://localhost:8501**

Default login:

- **Username**: `admin`
- **Password**: `admin`

Override credentials in `docker-compose.yml` or `.env`.

---

## 📂 Add Your PDFs

Put your walkthroughs into the `pdfs/` folder:

```bash
/pdfs
  ├── Blue_HTB_walkthrough.pdf
  ├── Forest_machine_notes.pdf
```

Use the **Reload PDFs** button to refresh the vectorstore.

---

## 🔐 Security

- No OpenAI/cloud APIs — all local
- Uses Ollama locally for inference
- Default login enabled — change password in env
- Recommended: Run behind Nginx + HTTPS for remote hosting

---

## 🌍 VPS Deployment (Nginx + SSL)

1. Clone repo on VPS
2. Install Nginx + Certbot
3. Proxy `localhost:8501` to your domain
4. Run `certbot --nginx` for free HTTPS

Ask me for full deploy tutorial if needed.

---

## 🧪 Unit Testing (Pytest)

Create `tests/` folder and use this pattern:

```bash
pip install pytest
pytest tests/
```

---

## 📄 License

MIT — Free to use, fork, and build upon.
