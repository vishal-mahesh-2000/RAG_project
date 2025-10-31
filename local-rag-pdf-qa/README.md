# Local RAG PDF Question Answering System

A local RAG (Retrieval-Augmented Generation) system for answering questions about PDF documents using Ollama LLM.

## Features

- PDF text extraction with OCR support
- Document embedding using sentence-transformers
- FAISS vector store for efficient similarity search
- Integration with Ollama for local LLM inference
- Streamlit web interface
- Configurable and extensible architecture

## Prerequisites

- Python 3.8+
- Tesseract OCR
- Ollama with llama2 model

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/local-rag-pdf-qa.git
cd local-rag-pdf-qa
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install the package:
```bash
pip install -e ".[dev]"
```

4. Copy the environment template:
```bash
cp config/.env.example .env
```

## Usage

1. Start the Streamlit interface:
```bash
streamlit run ui/streamlit_app.py
```

2. Upload a PDF document and ask questions about its content.

## Development

1. Run tests:
```bash
pytest
```

2. Format code:
```bash
black src tests
isort src tests
```

## Project Structure

```
local-rag-pdf-qa/
├── src/                   # Source code
├── tests/                 # Unit tests
├── ui/                    # Streamlit interface
├── data/                  # Data storage
├── config/                # Configuration files
└── logs/                  # Application logs
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.