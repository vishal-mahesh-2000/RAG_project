#!/bin/bash
# Quick Start Script for Local RAG PDF Q&A System
# Run this script to set up the project on macOS/Linux
# For Windows, follow the commands manually or use Git Bash

set -e  # Exit on error

echo "================================"
echo "Local RAG PDF Q&A - Quick Setup"
echo "================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python $python_version found"
echo ""

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✓ Pip upgraded"
echo ""

# Install dependencies
echo "Installing dependencies (this may take a few minutes)..."
pip install -r requirements.txt > /dev/null 2>&1
echo "✓ Dependencies installed"
echo ""

# Setup environment file
if [ ! -f "config/.env" ]; then
    echo "Setting up environment variables..."
    cp config/.env.example config/.env
    echo "⚠ Created config/.env - Please edit with your Tesseract path"
    echo "  For macOS: /usr/local/bin/tesseract"
    echo "  For Linux: /usr/bin/tesseract"
else
    echo "✓ Environment file already exists"
fi
echo ""

# Create data directories
echo "Creating data directories..."
mkdir -p data/pdfs data/faiss_indexes data/chat_history logs
echo "✓ Data directories created"
echo ""

# Check if test PDF exists
if [ ! -f "tests/data/sample.pdf" ]; then
    echo "⚠ No test PDF found in tests/data/sample.pdf"
    echo "  Add a sample PDF for testing"
else
    echo "✓ Test PDF found"
fi
echo ""

echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "Next steps:"
echo "1. Edit config/.env with your Tesseract path"
echo "2. Download Ollama models:"
echo "   ollama pull nomic-embed-text"
echo "   ollama pull mistral:7b-instruct-q4_K_M"
echo ""
echo "3. Start Ollama server in a new terminal:"
echo "   ollama serve"
echo ""
echo "4. Run the application:"
echo "   streamlit run ui/streamlit_app.py"
echo ""
echo "5. Run tests (optional):"
echo "   pytest tests/ -v"
echo ""
echo "Happy coding! 🚀"
