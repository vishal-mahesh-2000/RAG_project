# VS Code Setup Guide for Local RAG System

Complete step-by-step guide to set up and develop the Local RAG PDF Q&A system in VS Code.

## Prerequisites

- VS Code installed ([download here](https://code.visualstudio.com/))
- Python 3.11+ installed
- Git installed
- Ollama installed ([download here](https://ollama.ai))

## Step 1: Clone Repository in VS Code

### Method A: Using Git Bash

1. Open VS Code
2. Press `Ctrl+`` (backtick) to open terminal
3. Navigate to desired directory:
   ```bash
   cd your/desired/directory
   ```
4. Clone repository:
   ```bash
   git clone https://github.com/yourusername/local-rag-pdf-qa.git
   cd local-rag-pdf-qa
   ```

### Method B: Using VS Code UI

1. Press `Ctrl+Shift+P` to open Command Palette
2. Type "Git: Clone"
3. Paste repository URL: `https://github.com/yourusername/local-rag-pdf-qa.git`
4. Select destination folder
5. Click "Open" to open cloned repo

## Step 2: Install Required VS Code Extensions

1. Click Extensions icon (Ctrl+Shift+X)
2. Install the following extensions:

### Essential Extensions
- **Python** (Microsoft) - ID: `ms-python.python`
- **Pylance** (Microsoft) - ID: `ms-python.vscode-pylance`
- **Python Debugger** (Microsoft) - ID: `ms-python.debugpy`

### Recommended Extensions
- **Jupyter** (Microsoft) - ID: `ms-toolsai.jupyter` (for notebook support)
- **Pytest Explorer** (Little Foxes) - ID: `littlefoxteam.vscode-python-test-adapter`
- **Git Graph** (mhutchie) - ID: `mhutchie.git-graph`
- **GitLens** (eamodio) - ID: `eamodio.gitlens`
- **Prettier** (Prettier) - ID: `esbenp.prettier-vscode`
- **Thunder Client** - ID: `rangav.vscode-thunder-client` (for API testing)

Installation steps:
1. Find extension in marketplace
2. Click "Install"
3. Reload VS Code if prompted

## Step 3: Configure Python Interpreter

1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Click on suggested Python 3.11+
4. If not listed, click "Enter interpreter path..."
5. Navigate to your Python executable:
   - Windows: `C:\Python311\python.exe`
   - macOS: `/usr/local/bin/python3`
   - Linux: `/usr/bin/python3`

## Step 4: Create Virtual Environment in VS Code

1. Open terminal in VS Code: `Ctrl+``
2. Create virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. VS Code should automatically detect venv (check status bar)
4. If not, use "Python: Select Interpreter" and choose venv

## Step 5: Install Dependencies

1. Ensure venv is activated (check terminal shows `(venv)` prefix)
2. Run in terminal:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Wait for installation to complete (may take 2-3 minutes)
4. Verify installation:
   ```bash
   pip list | grep -E "streamlit|faiss|ollama"
   ```

## Step 6: Configure Project Settings

### VS Code Workspace Settings

1. Create file: `.vscode/settings.json` in project root
2. Add these settings:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.pylintArgs": ["--max-line-length=100"],
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "ms-python.python",
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnPaste": true
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/.*": true,
    "**/*.pyc": true
  },
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.analysis.typeCheckingMode": "basic"
}
```

### VS Code Launch Configuration

1. Create file: `.vscode/launch.json`
2. Add these configurations:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Streamlit UI",
      "type": "python",
      "request": "launch",
      "module": "streamlit",
      "args": ["run", "ui/streamlit_app.py"],
      "jinja": true,
      "justMyCode": false,
      "env": {
        "PYTHONPATH": "${workspaceFolder}",
        "DEBUG_MODE": "true"
      }
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Pytest: All Tests",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["tests/", "-v"],
      "console": "integratedTerminal",
      "justMyCode": false
    },
    {
      "name": "Pytest: Current File",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["${file}", "-v"],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

## Step 7: Configure Environment Variables

1. Copy example environment file:
   ```bash
   cp config/.env.example config/.env
   ```

2. Edit `.env` file:
   - On Windows, find Tesseract installation path
   - Update TESSERACT_CMD variable
   - Set other paths as needed

### Example `.env` for Windows:
```bash
OLLAMA_HOST=http://localhost:11434
OLLAMA_API_TIMEOUT=300
TESSERACT_CMD=C:\\Program Files\\Tesseract-OCR\\tesseract.exe
APP_ENV=development
DEBUG_MODE=false
```

### Example `.env` for macOS/Linux:
```bash
OLLAMA_HOST=http://localhost:11434
OLLAMA_API_TIMEOUT=300
TESSERACT_CMD=/usr/bin/tesseract
APP_ENV=development
DEBUG_MODE=false
```

## Step 8: Download Ollama Models

1. Open terminal (Ctrl+`)
2. Pull embedding model:
   ```bash
   ollama pull nomic-embed-text
   ```
3. Pull LLM model:
   ```bash
   ollama pull mistral:7b-instruct-q4_K_M
   ```
4. Verify models downloaded:
   ```bash
   ollama list
   ```

## Step 9: Start Ollama Server

1. Open new terminal in VS Code (Ctrl+Shift+`)
2. Run:
   ```bash
   ollama serve
   ```
3. Verify server running - should show:
   ```
   Listening on 127.0.0.1:11434
   ```
4. Leave this terminal running (don't close)

## Step 10: Run Application

### Option A: Run Streamlit UI

1. Open another terminal (Ctrl+Shift+`)
2. Make sure venv is activated
3. Run:
   ```bash
   streamlit run ui/streamlit_app.py
   ```
4. Browser should open to `http://localhost:8501`
5. If not, manually navigate to that URL

### Option B: Debug Run

1. Press `F5` or go to Run → Start Debugging
2. Select "Streamlit UI" from dropdown
3. Application starts with debugger attached
4. Can now set breakpoints and inspect variables

### Option C: Run Individual Python Files

1. Open any `.py` file
2. Press `Ctrl+F5` to run without debugging
3. Output appears in terminal

## Step 11: Set Up Testing

### Configure Pytest

1. Ensure pytest settings in `.vscode/settings.json`:
   ```json
   "python.testing.pytestEnabled": true,
   "python.testing.pytestArgs": ["tests"]
   ```

2. Click Testing icon in left sidebar (beaker icon)

3. Tests should appear in Test Explorer

### Run Tests

**Method A: Command Palette**
1. Press `Ctrl+Shift+P`
2. Type "Test: Run All Tests"

**Method B: Debug**
1. Press `F5`
2. Select "Pytest: All Tests" configuration

**Method C: Manual**
1. Open terminal
2. Run:
   ```bash
   pytest tests/ -v
   pytest tests/test_pdf_processor.py::TestPDFProcessor::test_processor_initialization -v
   ```

## Step 12: Git Workflow in VS Code

### Clone/Create Repository

1. Source Control icon (Ctrl+Shift+G)
2. Click "Initialize Repository" if new repo

### Commit Changes

1. Click Source Control icon
2. Stage changes: Click `+` next to files
3. Write commit message in text box
4. Press `Ctrl+Enter` or click commit button

### Create Branch

1. Click branch name in bottom left
2. Select "Create new branch..."
3. Enter branch name
4. Select base branch (usually main)

### Push to GitHub

1. Make commits
2. Click `...` menu in Source Control
3. Select "Push" or "Publish Branch"

### Pull Changes

1. Click `...` menu
2. Select "Pull"

## Step 13: Debugging Tips

### Set Breakpoints

1. Click line number in editor to add red dot (breakpoint)
2. Run with F5 (Streamlit UI configuration)
3. Execution pauses at breakpoint
4. Use Debug Console to inspect variables

### Debug Console

1. Press `Ctrl+Shift+Y` to open Debug Console
2. Type variable names to inspect
3. Example: `st.session_state` to inspect Streamlit state

### Log Messages

Add to code:
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Debug message here")
```

View in Output panel (Ctrl+Shift+U)

## Step 14: Common Workflows

### Add New Python Module

1. Right-click folder → "New File"
2. Name: `module_name.py`
3. Add docstring and type hints
4. Start coding

### Run Quick Test

1. Create temporary file: `test_quick.py`
2. Write test code
3. Press `Ctrl+F5` to run
4. Delete when done

### Install New Package

1. Open terminal
2. Ensure venv activated
3. Run: `pip install package_name`
4. VS Code should auto-detect and offer IntelliSense

### Format Code

1. Select code (or Ctrl+A for all)
2. Press `Shift+Alt+F`
3. Code auto-formats to style guide

### Find Issues

1. Press `Ctrl+Shift+M` to open Problems panel
2. View all linting errors
3. Click error to jump to code
4. Hover for suggested fixes

## Step 15: Productivity Shortcuts

| Action | Shortcut |
|--------|----------|
| Command Palette | Ctrl+Shift+P |
| Open File | Ctrl+O |
| Terminal | Ctrl+` |
| New Terminal | Ctrl+Shift+` |
| Debug | F5 |
| Stop Debug | Shift+F5 |
| Run Without Debug | Ctrl+F5 |
| Go to Definition | F12 |
| Find All References | Shift+F12 |
| Rename Symbol | F2 |
| Format Document | Shift+Alt+F |
| Git Commit | Ctrl+K, Ctrl+C |
| Source Control | Ctrl+Shift+G |
| Run Tests | Ctrl+Shift+P → "Test: Run All Tests" |

## Troubleshooting

### Python Interpreter Not Found

1. Ctrl+Shift+P → "Python: Select Interpreter"
2. Choose from list or "Enter interpreter path"
3. If venv shows, select it
4. Restart VS Code if needed

### Modules Not Found

1. Verify venv activated (shows `(venv)` in terminal)
2. Run: `pip install -r requirements.txt`
3. Reload VS Code (Ctrl+Shift+P → "Developer: Reload Window")

### Ollama Connection Error

1. Check Ollama running: `ollama list`
2. Verify OLLAMA_HOST in `.env` is correct
3. Try: `http://localhost:11434` or check Ollama settings

### Streamlit Port Already in Use

1. Kill process on port 8501
2. Or run on different port:
   ```bash
   streamlit run ui/streamlit_app.py --server.port 8502
   ```

### Can't Install Tesseract

- Windows: Download installer from GitHub
- macOS: `brew install tesseract`
- Linux: `sudo apt-get install tesseract-ocr`

### Permission Denied on macOS/Linux

```bash
chmod +x venv/bin/activate
chmod +x venv/bin/python
```

## Next Steps

1. ✅ Complete all steps above
2. 📚 Read `README.md` for architecture details
3. 🧪 Run tests: `pytest tests/ -v`
4. 🚀 Upload sample PDF and test chat
5. 📖 Explore source code in `src/` folder
6. 🔧 Modify `config/config.json` to experiment
7. 💬 Create feature branch and make improvements

## Support

- Check logs: `./logs/app.log`
- Review error messages in VS Code Output (Ctrl+Shift+U)
- Check terminal for stack traces
- Search Issues on GitHub repository

Happy coding! 🎉
