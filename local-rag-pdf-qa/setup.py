from setuptools import setup, find_packages

setup(
    name="local-rag-pdf-qa",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "sentence-transformers",
        "faiss-cpu",
        "PyMuPDF",
        "pytesseract",
        "pdf2image",
        "python-dotenv",
        "requests",
        "numpy",
        "pytest",
        "pytest-cov",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "flake8",
            "pytest",
            "pytest-cov",
        ]
    },
    python_requires=">=3.8",
)