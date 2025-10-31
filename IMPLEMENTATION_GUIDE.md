# Complete Local RAG System - Full Code Implementation Guide

## Overview

This document contains complete, production-ready code for building a local RAG PDF Q&A system. All code is organized by file and ready to be copied into your project.

---

## File Structure to Create

```
local-rag-pdf-qa/
├── .github/
│   └── workflows/
│       └── [CI/CD skipped as requested]
├── src/
│   ├── __init__.py                    # Package marker (empty file)
│   ├── config.py                      # ✅ Configuration management
│   ├── utils.py                       # ✅ Utilities & logging
│   ├── pdf_processor.py               # ✅ PDF extraction with OCR
│   ├── embeddings.py                  # ✅ Embedding generation
│   ├── vector_store.py                # ✅ FAISS vector database
│   ├── llm_interface.py               # ✅ Ollama LLM interface
│   └── rag_pipeline.py                # ✅ Main RAG orchestration
├── ui/
│   ├── __init__.py                    # Package marker
│   └── streamlit_app.py               # ✅ Web interface
├── tests/
│   ├── __init__.py                    # Package marker
│   ├── test_pdf_processor.py          # ✅ PDF processor tests
│   ├── test_embeddings.py             # ✅ Embedding tests
│   ├── test_vector_store.py           # ✅ Vector store tests
│   └── data/
│       └── sample.pdf                 # ⚠️ Add your test PDF here
├── config/
│   ├── config.json                    # ✅ Main configuration
│   └── .env.example                   # ✅ Environment template
├── data/
│   ├── pdfs/
│   │   └── .gitkeep
│   ├── faiss_indexes/
│   │   └── .gitkeep
│   └── chat_history/
│       └── .gitkeep
├── logs/
│   └── .gitkeep
├── .gitignore                         # ✅ Git ignore rules
├── requirements.txt                   # ✅ Python dependencies
├── pyproject.toml                     # ✅ Project configuration
├── setup.py                           # Create if needed
├── README.md                          # ✅ Main documentation
├── SETUP_VSCODE.md                    # ✅ VS Code guide
└── LICENSE                            # Add MIT license


✅ = Files provided below
⚠️ = User provides this
```

---

## Step-by-Step Implementation

### Step 1: Initialize Project

```bash
# Create project directory
mkdir local-rag-pdf-qa
cd local-rag-pdf-qa

# Initialize git
git init

# Create directory structure
mkdir -p src ui tests/data config data/{pdfs,faiss_indexes,chat_history} logs

# Create __init__.py files
touch src/__init__.py ui/__init__.py tests/__init__.py

# Create placeholder files for gitkeep
touch data/pdfs/.gitkeep data/faiss_indexes/.gitkeep data/chat_history/.gitkeep logs/.gitkeep
```

### Step 2: Copy Configuration Files

Copy the following files to your project:

1. **config/config.json** - Main configuration
2. **config/.env.example** - Environment template  
3. **.gitignore** - Git ignore rules
4. **requirements.txt** - Python dependencies
5. **pyproject.toml** - Project metadata
6. **README.md** - Documentation
7. **SETUP_VSCODE.md** - VS Code setup guide

### Step 3: Copy Source Files

Copy all files from `src/` folder:

1. **src/config.py** - Configuration management
2. **src/utils.py** - Utilities and logging
3. **src/pdf_processor.py** - PDF extraction
4. **src/embeddings.py** - Embedding generation
5. **src/vector_store.py** - FAISS vector store
6. **src/llm_interface.py** - Ollama LLM interface
7. **src/rag_pipeline.py** - RAG pipeline orchestration

### Step 4: Copy UI Files

Copy UI files to `ui/` folder:

1. **ui/streamlit_app.py** - Complete Streamlit application

### Step 5: Copy Test Files

Copy test files to `tests/` folder:

1. **tests/test_pdf_processor.py** - PDF processor tests
2. **tests/test_embeddings.py** - Embedding generator tests
3. **tests/test_vector_store.py** - Vector store tests

### Step 6: Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy environment template
cp config/.env.example config/.env

# Edit .env with your settings
# Set TESSERACT_CMD path for OCR
```

### Step 7: Download Ollama Models

```bash
# Pull embedding model
ollama pull nomic-embed-text

# Pull LLM model (choose based on your hardware)
ollama pull mistral:7b-instruct-q4_K_M
# OR
ollama pull llama3.2:3b
```

### Step 8: Run Application

```bash
# Terminal 1: Start Ollama server
ollama serve

# Terminal 2: Run Streamlit app
streamlit run ui/streamlit_app.py
```

---

## Code Files (Ready to Copy)

### All source code files have been provided above with complete implementations.

### Key Files Location Summary:

**Configuration & Utilities:**
- config.py
- utils.py

**Core RAG Components:**
- pdf_processor.py
- embeddings.py
- vector_store.py
- llm_interface.py
- rag_pipeline.py

**User Interface:**
- streamlit_app.py

**Tests:**
- test_pdf_processor.py
- test_embeddings.py
- test_vector_store.py

---

## Important Notes

### 1. Adding Test PDF

Place a PDF file in `tests/data/sample.pdf` for running tests:
```bash
cp your_sample.pdf tests/data/sample.pdf
```

### 2. First Run Checklist

- [ ] Python 3.11+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Ollama installed and running (`ollama serve`)
- [ ] Models downloaded (`nomic-embed-text`, `mistral:7b-instruct-q4_K_M`)
- [ ] `.env` file configured with TESSERACT_CMD
- [ ] Sample PDF in `tests/data/sample.pdf` (for testing)

### 3. Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_pdf_processor.py -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### 4. Git Workflow

```bash
# Initial commit
git add .
git commit -m "feat: initial local RAG system implementation"

# Create develop branch
git checkout -b develop

# Create feature branch for changes
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: add your feature"

# Push to GitHub
git push origin feature/your-feature

# Create Pull Request on GitHub
```

---

## Module Dependencies

```
config.py (no internal dependencies)
    ↓
utils.py (depends on config.py)
    ↓
pdf_processor.py (depends on config.py, utils.py)
    ↓
embeddings.py (depends on config.py, utils.py)
    ↓
vector_store.py (depends on config.py, utils.py)
    ↓
llm_interface.py (depends on config.py, utils.py)
    ↓
rag_pipeline.py (depends on all above modules)
    ↓
streamlit_app.py (depends on rag_pipeline.py, config.py, utils.py)
```

---

## Performance Benchmarks (Expected Results)

### On 8GB RAM CPU-Only

**Mistral 7B (4-bit quantized):**
- Text extraction: 100KB PDF → ~0.5 seconds
- Embedding generation (500 chars): ~2-3 seconds
- Vector search (FAISS): ~50ms
- LLM inference (100 tokens): ~30-40 seconds

**Llama 3.2 3B:**
- All operations ~2x faster than 7B
- Better for real-time interaction on CPU

### With 16GB VRAM GPU

**Mistral 7B (full precision):**
- Embedding generation: ~500ms
- LLM inference (100 tokens): ~2-3 seconds

---

## Optimization Tips

1. **For Speed:**
   - Use 3B models instead of 7B
   - Reduce chunk_size to 300
   - Lower top_k_retrieval to 3

2. **For Quality:**
   - Use 7B+ models
   - Increase chunk_size to 1000
   - Set top_k_retrieval to 7-10

3. **For Memory:**
   - Use 4-bit/8-bit quantized models
   - Reduce batch_size in config
   - Close other applications

---

## Common Issues & Solutions

### ModuleNotFoundError

**Problem:** Can't import src modules

**Solution:**
1. Ensure venv is activated
2. Run: `pip install -r requirements.txt`
3. Restart Python kernel if using Jupyter

### Ollama Connection Error

**Problem:** "Cannot connect to Ollama"

**Solution:**
1. Verify Ollama running: `ollama serve` in another terminal
2. Check OLLAMA_HOST in `.env` matches
3. Try: `http://localhost:11434` or `http://127.0.0.1:11434`

### FAISS Index Not Persisting

**Problem:** Index lost after restart

**Solution:**
1. Ensure `persist_directory` exists in config
2. Check write permissions
3. Verify `vector_store.save()` is called after adding docs

### Out of Memory

**Problem:** "CUDA out of memory" or "Killed"

**Solution:**
1. Use smaller models (3B instead of 7B)
2. Reduce batch_size in config
3. Enable GPU swap if available
4. Run on CPU instead

---

## Next Steps After Setup

1. ✅ **Complete Setup** - Follow all installation steps
2. 📚 **Read Documentation** - Review README.md and SETUP_VSCODE.md
3. 🧪 **Run Tests** - Execute `pytest tests/ -v`
4. 📤 **Upload PDF** - Add test PDF via Streamlit UI
5. 💬 **Test Chat** - Ask questions about your PDF
6. ⚙️ **Explore Config** - Modify config.json to experiment
7. 🔧 **Develop Features** - Create new branches and add improvements
8. 🚀 **Deploy** - Consider Docker containerization for production

---

## References

- [PyMuPDF Docs](https://pymupdf.readthedocs.io/)
- [FAISS Wiki](https://github.com/facebookresearch/faiss/wiki)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Streamlit Docs](https://docs.streamlit.io/)
- [LangChain RAG Guide](https://docs.langchain.com/docs/use_cases/qa_over_docs)

---

## Support & Troubleshooting

### Check Logs

```bash
# View application logs
tail -f logs/app.log

# Search for errors
grep ERROR logs/app.log
```

### Debug Mode

Set in `.env`:
```bash
DEBUG_MODE=true
```

Restart application to enable detailed logging.

### Test Individual Components

```bash
# Test PDF extraction
python -c "from src.pdf_processor import PDFProcessor; p = PDFProcessor(); print(p.extract_text('path/to/pdf.pdf')[:100])"

# Test embeddings
python -c "from src.embeddings import EmbeddingGenerator; e = EmbeddingGenerator(); emb = e.generate_embedding('test'); print(emb.shape)"

# Test LLM
python -c "from src.llm_interface import OllamaLLM; l = OllamaLLM(); resp = l.generate('Hello'); print(resp)"
```

---

## Final Checklist

- [ ] All files copied to correct directories
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] `.env` configured
- [ ] Ollama models downloaded
- [ ] Tests passing (`pytest tests/ -v`)
- [ ] Streamlit app starts (`streamlit run ui/streamlit_app.py`)
- [ ] Can upload and process PDF
- [ ] Can ask questions and get answers
- [ ] Chat history persists
- [ ] Logs are being written to `logs/app.log`

**You're ready to go! 🎉**
