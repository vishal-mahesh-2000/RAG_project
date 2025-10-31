"""Streamlit UI for the RAG application."""

import streamlit as st
from pathlib import Path
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import Config
from src.rag_pipeline import RAGPipeline
from src.utils import ensure_directory

# Initialize config and RAG pipeline
config = Config("config/config.json")
pipeline = RAGPipeline(config)

st.title("PDF Question Answering System")

# File upload
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file:
    # Save uploaded file
    save_dir = "data/pdfs"
    ensure_directory(save_dir)
    pdf_path = os.path.join(save_dir, uploaded_file.name)
    
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process document
    with st.spinner("Processing PDF..."):
        pipeline.process_document(pdf_path)
    st.success("PDF processed successfully!")

# Question input
question = st.text_input("Ask a question about your document")

if question:
    with st.spinner("Generating answer..."):
        answer = pipeline.query(question)
    st.write("Answer:", answer)