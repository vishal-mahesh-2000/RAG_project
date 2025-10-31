# Local RAG PDF Q&A System

**🔒 Private • Secure • Offline - All data stays on your machine**

A complete end-to-end Retrieval-Augmented Generation (RAG) system for question-answering over PDF documents using entirely local LLMs and vector databases. Perfect for confidential documents that must never leave your system.

## Features

✅ **100% Local Processing** - No API calls, no cloud uploads, complete privacy  
✅ **OCR Support** - Extract text from scanned PDFs using Tesseract  
✅ **FAISS Vector Database** - High-performance similarity search  
✅ **Multiple LLM Support** - Works with any Ollama model (Mistral, Llama, etc.)  
✅ **Streamlit UI** - Beautiful, intuitive web interface  
✅ **Chat History** - Persistent conversation history across sessions  
✅ **Batch Processing** - Upload and process multiple PDFs at once  
✅ **Performance Monitoring** - Memory tracking and execution metrics  
✅ **Comprehensive Logging** - Detailed logs for debugging and monitoring  
✅ **Cross-Platform** - Works on Windows, macOS, and Linux  

## Architecture

```
Local RAG System Architecture:
├── PDF Processor (PyMuPDF + Tesseract OCR)
├── Text Chunking (Configurable chunk size)
├── Embedding Generation (Ollama embeddings)
├── FAISS Vector Store (Persistent index)
├── LLM Interface (Ollama)
├── RAG Pipeline (Orchestration)
└── Streamlit UI (Web interface)

All components run locally - no external services required.
```

## System Requirements

### Minimum Configuration
- **RAM**: 8GB system memory
- **CPU**: 4+ cores (Intel i5/AMD Ryzen 5)
- **Storage**: 20GB free space (for models)
- **OS**: Windows 10+, macOS 10.15+, Ubuntu 20.04+

### Recommended Configuration
- **RAM**: 16GB system memory
- **CPU**: 8+ cores
- **Storage**: 50GB free space (SSD preferred)

### For Better Performance
- **GPU**: NVIDIA RTX 4060 Ti 16GB or better (optional but recommended)

## Quick Start

### 1. Prerequisites

Ensure you have:
- Python 3.11+
- Git
- Ollama installed ([download here](https://ollama.ai))

### 2. Clone Repository

```bash
git clone https://github.com/yourusername/local-rag-pdf-qa.git
cd local-rag-pdf-qa
```

### 3. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download Ollama Models

```bash
# Download embedding model
ollama pull nomic-embed-text

# Download LLM model (choose one)
ollama pull mistral:7b-instruct-q4_K_M
# OR
ollama pull llama3.2:3b
```

### 6. Configure Environment

```bash
cp config/.env.example config/.env
# Edit config/.env with your settings (especially Tesseract path on Windows)
```

### 7. Run Ollama

In a separate terminal:
```bash
ollama serve
```

### 8. Start Application

```bash
streamlit run ui/streamlit_app.py
```

Open your browser to `http://localhost:8501`

## Configuration

### Main Configuration File: `config/config.json`

```json
{
  "embedding": {
    "model_name": "nomic-embed-text",      // Embedding model
    "dimension": 768,                      // Embedding dimension
    "batch_size": 32                       // Batch processing size
  },
  "llm": {
    "model_name": "mistral:7b-instruct-q4_K_M",  // LLM model
    "temperature": 0.7,                   // Response creativity
    "max_tokens": 2048,                   // Max response length
    "context_window": 4096                // Model context window
  },
  "rag": {
    "chunk_size": 500,                    // Text chunk size (chars)
    "chunk_overlap": 50,                  // Chunk overlap for context
    "top_k_retrieval": 5,                 // Top-K chunks to retrieve
    "score_threshold": 0.3                // Minimum relevance score
  },
  "faiss": {
    "index_type": "IndexFlatL2",          // FAISS index type
    "persist_directory": "./data/faiss_indexes",
    "normalize_embeddings": true          // L2 normalization
  },
  "logging": {
    "level": "INFO",
    "file_path": "./logs/app.log",
    "max_bytes": 10485760,                // 10MB
    "backup_count": 5
  }
}
```

### Environment Variables: `config/.env`

```bash
# Ollama Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_API_TIMEOUT=300

# Tesseract OCR (required for scanned PDFs)
# Windows: C:\\Program Files\\Tesseract-OCR\\tesseract.exe
# Linux: /usr/bin/tesseract
# macOS: /usr/local/bin/tesseract
TESSERACT_CMD=/usr/bin/tesseract

# Application Settings
APP_ENV=development
DEBUG_MODE=false
```

## Model Selection Guide

### For CPU-Only (Recommended for 8GB RAM)
- **Embedding**: `nomic-embed-text` (768 dims, lightweight)
- **LLM**: `mistral:7b-instruct-q4_K_M` (7B params, 4-bit quantized)
- **Alternative LLM**: `llama3.2:3b` (3B params, very fast)

### For GPU (16GB VRAM)
- **Embedding**: `mxbai-embed-large` (1024 dims, high quality)
- **LLM**: `mistral:7b` (full precision)
- **Alternative**: `llama3:8b`

### For High-End GPU (24GB+ VRAM)
- **Embedding**: `mxbai-embed-large`
- **LLM**: `llama3:70b` (quantized or full)
- **Alternative**: `mixtral:8x7b`

## Usage Guide

### Upload and Process PDFs

1. **Single PDF Upload**
   - Go to "Documents" tab
   - Click "Upload Single PDF"
   - Select PDF and click "Upload and Process"

2. **Batch Upload**
   - Go to "Documents" → "Batch Upload"
   - Select multiple PDFs
   - Click "Upload and Process All"

### Ask Questions

1. **Chat Interface**
   - Go to "Chat" tab
   - Type your question
   - AI searches indexed PDFs and generates answer
   - View retrieved source chunks

### View Statistics

- **Stats** tab shows vector store metrics
- Memory usage and system information
- Document inventory

## Project Structure

```
local-rag-pdf-qa/
├── src/
│   ├── config.py              # Configuration management
│   ├── pdf_processor.py       # PDF extraction + OCR
│   ├── embeddings.py          # Embedding generation
│   ├── vector_store.py        # FAISS vector database
│   ├── llm_interface.py       # Ollama LLM interface
│   ├── rag_pipeline.py        # RAG orchestration
│   └── utils.py               # Utilities & logging
├── ui/
│   └── streamlit_app.py       # Web interface
├── tests/
│   ├── test_pdf_processor.py  # PDF processor tests
│   ├── test_embeddings.py     # Embedding tests
│   ├── test_vector_store.py   # Vector store tests
│   └── data/
│       └── sample.pdf         # Test PDF
├── config/
│   ├── config.json            # Main configuration
│   └── .env.example           # Environment template
├── data/
│   ├── pdfs/                  # User PDFs (gitignored)
│   ├── faiss_indexes/         # Vector indexes (gitignored)
│   └── chat_history/          # Chat sessions (gitignored)
├── logs/                      # Application logs (gitignored)
├── requirements.txt           # Python dependencies
├── pyproject.toml             # Project metadata
├── README.md                  # This file
└── SETUP_VSCODE.md            # VS Code setup guide
```

## Testing

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test Module

```bash
pytest tests/test_pdf_processor.py -v
pytest tests/test_embeddings.py -v
pytest tests/test_vector_store.py -v
```

### Run with Coverage

```bash
pytest tests/ --cov=src --cov-report=html
```

Coverage report will be generated in `htmlcov/index.html`

## Troubleshooting

### Ollama Connection Error
- Ensure Ollama is running: `ollama serve`
- Verify OLLAMA_HOST in `.env` matches your setup
- Check firewall isn't blocking port 11434

### Out of Memory Errors
- Use smaller LLM model (3B instead of 7B)
- Reduce batch_size in config.json
- Close other applications

### Tesseract OCR Not Found
- **Windows**: Install from https://github.com/UB-Mannheim/tesseract/wiki
- **Linux**: `sudo apt-get install tesseract-ocr`
- **macOS**: `brew install tesseract`
- Set TESSERACT_CMD in `.env` to installation path

### PDF Text Extraction Issues
- Check PDF is not encrypted
- Try enabling OCR in config.json
- Verify PDF file is not corrupted

### Slow Inference
- Consider using quantized models
- Increase batch_size for embeddings
- Use GPU if available

## Performance Optimization

### 1. Use Quantized Models
Quantized models (4-bit, 8-bit) run significantly faster with minimal quality loss:
```bash
ollama pull mistral:7b-instruct-q4_K_M  # 4-bit quantized
ollama pull mistral:7b-instruct-q5_K_M  # 5-bit quantized
```

### 2. Adjust Chunk Size
- Smaller chunks (300-400): Faster retrieval, less context
- Larger chunks (1000-1500): More context, slower retrieval

### 3. Reduce Top-K Retrieval
Lower `top_k_retrieval` in config.json to retrieve fewer chunks, reducing LLM processing time.

### 4. Enable GPU Acceleration
If you have NVIDIA GPU:
```bash
ollama pull mistral:7b  # GPU-optimized version
```

## Privacy & Security

✅ **No Network Communication** - All processing stays local  
✅ **No Data Collection** - No telemetry or tracking  
✅ **No Cloud Uploads** - PDFs never leave your machine  
✅ **Model Weights Frozen** - LLM cannot learn from your data  
✅ **Local Embeddings** - Vector DB stores only on disk  

All data is stored in `./data/` directory on your machine.

## Development

### Create New Branch for Features

```bash
git checkout -b feature/your-feature-name
```

### Commit Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

### Push to GitHub

```bash
git push origin feature/your-feature-name
```

### Create Pull Request on GitHub

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support & Issues

For issues, questions, or suggestions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include error logs and system information

## Roadmap

- [ ] Docker containerization
- [ ] REST API interface
- [ ] Advanced query syntax
- [ ] Multi-language support
- [ ] Hybrid search (keyword + semantic)
- [ ] Document versioning
- [ ] Collaborative features

## Acknowledgments

Built with:
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF processing
- [Ollama](https://ollama.ai) - Local LLM inference
- [FAISS](https://faiss.ai/) - Vector search
- [Streamlit](https://streamlit.io/) - Web UI
- [Tesseract](https://tesseract-ocr.github.io/) - OCR

## References

- [RAG Best Practices](https://docs.llamaindex.ai/en/stable/)
- [FAISS Documentation](https://faiss.ai/index.html)
- [Ollama Models](https://ollama.ai/library)
- [Streamlit Docs](https://docs.streamlit.io/)
