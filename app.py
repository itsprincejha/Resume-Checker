import streamlit as st
from dotenv import load_dotenv
import os
import tempfile
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

YOUR_GROQ_API_KEY_ = os.getenv("GROQ_API_KEY")

st.title("FREE Resume Checker – RAG App 💻 (LLaMA 3.1)")

# Groq client
client = Groq(api_key=YOUR_GROQ_API_KEY_)

# Upload PDF
uploaded = st.file_uploader("Upload your resume PDF", type="pdf")

if uploaded is not None:
    # Save uploaded PDF as a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(uploaded.read())
        temp_path = temp.name

    # Load the PDF
    loader = PyPDFLoader(temp_path)
    docs = loader.load()

    st.success("PDF loaded successfully!")

    # Split text
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

     # Embedding model
    embedding_model =  HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    

    # Vector DB
    vectordb = Chroma.from_documents(chunks, embedding=embedding_model)

    question = "Give 5 improvements for this resume for a Data Analyst role."
    similar = vectordb.similarity_search(question)

    context = " ".join([d.page_content for d in similar])

    prompt = f"""
    You are a resume expert.
    Resume Content:
    {context}

    Task:
    {question}

    Answer in bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("Resume Improvement Suggestions 🎯:")
    st.write(response.choices[0].message.content)





    


