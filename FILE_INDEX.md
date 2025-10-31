# Local RAG PDF Q&A System - Complete Documentation Index

## 📖 Documentation Files Map

### Quick References
| File | Purpose | Read Time |
|------|---------|-----------|
| **DELIVERY_SUMMARY.md** | Overview of what's delivered | 5 min |
| **README.md** | Full project documentation | 15 min |
| **SETUP_VSCODE.md** | VS Code setup guide | 20 min |
| **IMPLEMENTATION_GUIDE.md** | Complete implementation walkthrough | 30 min |
| **This File** | Documentation index and file map | 5 min |

---

## 🗂️ Complete File Structure

```
local-rag-pdf-qa/
│
├── 📄 Configuration Files
│   ├── config/config.json              Configuration (embedding, LLM, RAG, logging)
│   ├── config/.env.example             Environment template
│   ├── .gitignore                      Git ignore rules
│   ├── requirements.txt                Python dependencies
│   └── pyproject.toml                  Project metadata & build config
│
├── 🐍 Source Code (src/)
│   ├── src/__init__.py                 Package marker
│   ├── src/config.py                   Configuration management
│   ├── src/utils.py                    Logging, monitoring, utilities
│   ├── src/pdf_processor.py            PDF extraction with OCR
│   ├── src/embeddings.py               Ollama embedding generation
│   ├── src/vector_store.py             FAISS vector database
│   ├── src/llm_interface.py            Ollama LLM interface
│   └── src/rag_pipeline.py             RAG orchestration (main logic)
│
├── 🎨 User Interface (ui/)
│   ├── ui/__init__.py                  Package marker
│   └── ui/streamlit_app.py             Web interface (complete app)
│
├── 🧪 Tests (tests/)
│   ├── tests/__init__.py               Package marker
│   ├── tests/test_pdf_processor.py     PDF processor tests
│   ├── tests/test_embeddings.py        Embedding generator tests
│   ├── tests/test_vector_store.py      Vector store tests
│   └── tests/data/sample.pdf           Test PDF (user provides)
│
├── 💾 Data & Logs (auto-created)
│   ├── data/pdfs/                      User uploads
│   ├── data/faiss_indexes/             Vector indexes
│   ├── data/chat_history/              Session history
│   └── logs/app.log                    Application logs
│
└── 📚 Documentation
    ├── README.md                       Main documentation
    ├── SETUP_VSCODE.md                 VS Code setup guide
    ├── IMPLEMENTATION_GUIDE.md         Implementation walkthrough
    ├── DELIVERY_SUMMARY.md             What's delivered
    ├── setup.sh                        Auto-setup script (macOS/Linux)
    └── FILE_INDEX.md                   This file
```

---

## 📚 Reading Guide by Use Case

### "I Want to Set Up and Run the Project"
1. **Start**: DELIVERY_SUMMARY.md (quick overview)
2. **Setup**: SETUP_VSCODE.md (VS Code setup)
3. **Run**: README.md (Quick Start section)
4. **Reference**: IMPLEMENTATION_GUIDE.md (detailed steps)

### "I Want to Understand the Architecture"
1. **Overview**: README.md (Architecture section)
2. **Details**: IMPLEMENTATION_GUIDE.md (Module dependencies)
3. **Code**: Read src/rag_pipeline.py (main orchestrator)

### "I Want to Modify/Extend the Code"
1. **Start**: SETUP_VSCODE.md (development setup)
2. **Understand**: README.md (architecture)
3. **Code**: Read specific modules in src/
4. **Test**: tests/ folder (understand patterns)

### "I'm Troubleshooting an Issue"
1. **Quick**: DELIVERY_SUMMARY.md (Troubleshooting table)
2. **Detailed**: README.md (Troubleshooting section)
3. **Debug**: Check logs/app.log
4. **Code**: Review relevant module in src/

---

## 🔑 Key Files Explained

### Configuration
**config/config.json** - ALL settings in one file
- Embedding model (currently: nomic-embed-text, 768 dims)
- LLM model (currently: mistral:7b-instruct-q4_K_M)
- RAG parameters (chunk size: 500, top_k: 5)
- Logging configuration
- Performance settings

**config/.env** - Sensitive/machine-specific settings
- OLLAMA_HOST (where Ollama runs)
- TESSERACT_CMD (path to OCR tool)
- DEBUG_MODE (true/false)

### Core Modules
**src/rag_pipeline.py** - Entry point for all RAG operations
- add_document() - Process and index a PDF
- query() - Ask a question
- list_documents() - View all indexed PDFs
- get_stats() - System statistics

**src/pdf_processor.py** - PDF text extraction
- extract_text() - Get text with OCR fallback
- chunk_text() - Split into chunks
- Handles scanned PDFs via Tesseract

**src/embeddings.py** - Text to vectors
- generate_embedding() - Single embedding
- generate_embeddings_batch() - Multiple embeddings
- Uses Ollama local model

**src/vector_store.py** - Vector database
- add_documents() - Store embeddings
- search() - Find similar chunks
- save/load() - Persist to disk
- Uses FAISS for similarity search

**src/llm_interface.py** - LLM inference
- generate() - Text generation
- chat() - Chat completion
- create_rag_prompt() - Format context + question
- Uses Ollama local LLM

### User Interface
**ui/streamlit_app.py** - Web application
- Chat page: Talk to PDFs
- Documents page: Upload and manage PDFs
- Settings page: View configuration
- Stats page: System metrics

---

## 🚀 Quick Start Paths

### Path 1: Automated Setup (Easiest)
```bash
chmod +x setup.sh              # Make executable
./setup.sh                     # Auto-setup everything
# Then follow the prompts
```

### Path 2: Manual Setup (Recommended for Windows)
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
cp config/.env.example config/.env
# Edit config/.env with Tesseract path
```

### Path 3: Docker Setup (Future)
```bash
docker build -t local-rag .
docker run -p 8501:8501 local-rag
```

---

## 📋 Development Workflow

### First Time Setup (15 minutes)
1. Clone repo: `git clone <url>`
2. Run setup: `./setup.sh` or follow Path 2
3. Download models: `ollama pull nomic-embed-text && ollama pull mistral:7b-instruct-q4_K_M`
4. Start Ollama: `ollama serve` (in separate terminal)
5. Launch app: `streamlit run ui/streamlit_app.py`

### Daily Development (after setup)
1. Activate venv: `source venv/bin/activate`
2. Make changes to code
3. Run tests: `pytest tests/ -v`
4. Test locally: `streamlit run ui/streamlit_app.py`
5. Commit changes: `git add . && git commit -m "message"`

### Adding New Features
1. Create branch: `git checkout -b feature/your-feature`
2. Implement in relevant module
3. Add tests for new functionality
4. Update config.json if needed
5. Test thoroughly
6. Commit and push
7. Create pull request

---

## 🔍 Module Dependency Tree

```
config.py
  └─ Provides: Configuration singleton

utils.py
  └─ Depends: config.py
  └─ Provides: Logging, performance monitoring

pdf_processor.py
  └─ Depends: config.py, utils.py
  └─ Provides: Text extraction, chunking, OCR

embeddings.py
  └─ Depends: config.py, utils.py
  └─ Provides: Embedding generation via Ollama

vector_store.py
  └─ Depends: config.py, utils.py
  └─ Provides: FAISS vector database with persistence

llm_interface.py
  └─ Depends: config.py, utils.py
  └─ Provides: Ollama LLM interface

rag_pipeline.py
  └─ Depends: pdf_processor, embeddings, vector_store, llm_interface
  └─ Provides: Main RAG orchestration

streamlit_app.py
  └─ Depends: rag_pipeline, config, utils
  └─ Provides: Web user interface
```

---

## 🧪 Testing Guide

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_pdf_processor.py -v
pytest tests/test_embeddings.py -v
pytest tests/test_vector_store.py -v
```

### Run Specific Test
```bash
pytest tests/test_vector_store.py::TestFAISSVectorStore::test_add_documents -v
```

### Run with Coverage Report
```bash
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html to view
```

### Test Organization
- `test_pdf_processor.py` - 7 tests for PDF extraction
- `test_embeddings.py` - 6 tests for embedding generation
- `test_vector_store.py` - 11 tests for vector storage

Total: 24 unit tests

---

## 📊 Configuration Reference

### Essential Configuration
```json
{
  "embedding": {
    "model_name": "nomic-embed-text",   // For 8GB RAM
    "dimension": 768
  },
  "llm": {
    "model_name": "mistral:7b-instruct-q4_K_M",  // For 8GB RAM
    "temperature": 0.7
  },
  "rag": {
    "chunk_size": 500,                  // Smaller = faster search
    "top_k_retrieval": 5                // More = slower but better context
  }
}
```

### For Better Performance
- Use GPU: Set CUDA environment variables
- Reduce chunk_size to 300
- Reduce top_k to 3
- Use quantized models

### For Better Quality
- Increase chunk_size to 1000
- Increase top_k to 10
- Use larger models (7B+)
- Disable quantization

---

## 🎯 Common Tasks

### Upload and Index a PDF
```python
from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()
doc_id = rag.add_document("path/to/document.pdf")
print(f"Document indexed: {doc_id}")
```

### Query Documents
```python
result = rag.query("What is this document about?")
print(result['answer'])
print(f"Retrieved {result['retrieved_chunks']} chunks")
for source in result['sources']:
    print(f"  - {source['text'][:100]}...")
```

### List Indexed Documents
```python
documents = rag.list_documents()
for doc in documents:
    print(f"{doc['filename']}: {doc['num_chunks']} chunks")
```

### Get System Statistics
```python
stats = rag.get_stats()
print(f"Total vectors: {stats['vector_store']['total_vectors']}")
print(f"Documents: {stats['vector_store']['total_documents']}")
```

---

## ⚙️ Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| OLLAMA_HOST | http://localhost:11434 | Ollama API endpoint |
| OLLAMA_API_TIMEOUT | 300 | Request timeout (seconds) |
| TESSERACT_CMD | /usr/bin/tesseract | OCR executable path |
| APP_ENV | development | Environment (dev/prod) |
| DEBUG_MODE | false | Enable debug logging |

---

## 📞 Support Resources

### If Code Won't Run
1. Check `logs/app.log` for errors
2. Verify Ollama running: `ollama list`
3. Check Python version: `python --version`
4. Reinstall deps: `pip install -r requirements.txt`

### If Tests Fail
1. Ensure venv activated
2. Run individual test: `pytest tests/test_file.py -v`
3. Check Ollama mock in tests
4. Review test output for details

### If Performance is Slow
1. Check CPU/memory usage
2. Reduce chunk_size in config
3. Reduce top_k in config
4. Use smaller LLM model
5. Enable GPU if available

### If PDF Extraction Fails
1. Check PDF is not corrupted
2. Verify not encrypted
3. Try enabling OCR
4. Check PDF format (PDF text vs scanned)

---

## 🎓 Learning Path

### Beginner
1. Read DELIVERY_SUMMARY.md
2. Follow SETUP_VSCODE.md
3. Run the application
4. Upload a PDF and ask questions

### Intermediate
1. Read README.md
2. Explore config/config.json
3. Modify settings and experiment
4. Run tests to understand structure

### Advanced
1. Read IMPLEMENTATION_GUIDE.md
2. Study source code in src/
3. Write custom code using RAG pipeline
4. Extend functionality

### Expert
1. Modify embedding model
2. Fine-tune RAG parameters
3. Implement custom components
4. Contribute improvements

---

## 📈 Performance Optimization Checklist

- [ ] Using quantized model (4-bit/8-bit)
- [ ] Chunk size optimized for your PDFs
- [ ] Top-k reduced to minimum needed
- [ ] Ollama running with GPU if available
- [ ] No other heavy processes running
- [ ] Sufficient disk space for indexes
- [ ] RAM usage monitored

---

## ✅ Pre-Launch Checklist

- [ ] All files copied to correct locations
- [ ] Virtual environment created and activated
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] config/.env created from .env.example
- [ ] Tesseract path set correctly in .env
- [ ] Ollama installed and models downloaded
- [ ] `ollama serve` running in separate terminal
- [ ] Tests passing: `pytest tests/ -v`
- [ ] Sample PDF in tests/data/sample.pdf
- [ ] Streamlit runs: `streamlit run ui/streamlit_app.py`
- [ ] Can upload PDF via UI
- [ ] Can ask questions and get answers
- [ ] Chat history persists
- [ ] Logs writing to logs/app.log

---

## 🎉 You're Ready!

All documentation is in place. Start with **DELIVERY_SUMMARY.md** then follow the reading guide for your use case.

**Main Entry Points:**
1. **To Run**: Follow README.md Quick Start
2. **To Develop**: Read SETUP_VSCODE.md
3. **To Understand**: Read IMPLEMENTATION_GUIDE.md
4. **To Customize**: Edit config/config.json

**Happy coding! 🚀**
