"""Tests for PDF processor."""

import pytest
from src.pdf_processor import PDFProcessor
from src.config import Config
import os

@pytest.fixture
def config():
    return Config("config/config.json")

@pytest.fixture
def processor(config):
    return PDFProcessor(config)

def test_extract_text_directly(processor):
    pdf_path = os.path.join("tests", "data", "sample.pdf")
    text = processor._extract_text_directly(pdf_path)
    assert isinstance(text, str)
    assert len(text) > 0

def test_extract_text_with_ocr(processor):
    pdf_path = os.path.join("tests", "data", "sample.pdf")
    text = processor._extract_text_with_ocr(pdf_path)
    assert isinstance(text, str)
    assert len(text) > 0