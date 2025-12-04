# Resume-Checker
A friendly, interactive AI Resume Checker built with Streamlit and Groq’s LLaMA 3.1 model. 


# 🧠 RAG-Based Document Question Answering System  
A Retrieval-Augmented Generation (RAG) application that allows users to upload documents (PDF/Text) and get accurate answers using vector embeddings and an LLM.

---

## 🚀 Project Overview
This project demonstrates how to build an end-to-end **RAG pipeline** using:

- Document loaders  
- Text chunking  
- Embedding generation  
- Vector storage (ChromaDB)  
- Retrieval + LLM answer generation  

The system takes any user-uploaded document and intelligently answers questions based on the document content.

---

## 🛠 Tech Stack
| Component | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| Embeddings | HuggingFace BGE Sentence Embeddings |
| Vector Store | ChromaDB |
| LLM | Groq / OpenAI / Any LLM (configurable) |
| UI (Optional) | Streamlit |
| Environment | dotenv |

---

## ✨ Features
- 📄 Upload any PDF or text document  
- 🔍 Automatically extracts and chunks text  
- 🧠 Generates semantic embeddings  
- 📦 Stores embeddings in a local vector database  
- 🤖 Uses RAG pipeline to answer questions accurately  
- ⚡ Fast embedding generation using HuggingFace (no API needed)  
- 🔑 Supports OpenAI/Groq API for LLM generation  

---
## 🚀 Live Demo  
👉 [Click here to open the Live App]:https://resume-smart.streamlit.app/


