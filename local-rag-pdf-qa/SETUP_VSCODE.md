# VS Code Setup Guide

This guide helps you set up Visual Studio Code for development on this project.

## Required Extensions

1. Python
```
ms-python.python
```

2. Pylance
```
ms-python.vscode-pylance
```

3. Python Test Explorer
```
littlefoxteam.vscode-python-test-adapter
```

4. Black Formatter
```
ms-python.black-formatter
```

## Recommended Settings

Add these to your workspace settings (`.vscode/settings.json`):

```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.analysis.typeCheckingMode": "basic"
}
```

## Debug Configuration

Add this launch configuration (`.vscode/launch.json`):

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Streamlit",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "args": ["run", "ui/streamlit_app.py"],
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```