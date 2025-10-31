"""PDF Processor module for extracting text from PDFs using OCR."""

import pytesseract
from pdf2image import convert_from_path
import fitz  # PyMuPDF

class PDFProcessor:
    def __init__(self, config):
        self.config = config
        
    def extract_text(self, pdf_path):
        """Extract text from PDF using OCR if needed."""
        text = self._extract_text_directly(pdf_path)
        if not text.strip():
            text = self._extract_text_with_ocr(pdf_path)
        return text
    
    def _extract_text_directly(self, pdf_path):
        """Try to extract text directly from PDF."""
        text = ""
        with fitz.open(pdf_path) as pdf:
            for page in pdf:
                text += page.get_text()
        return text
    
    def _extract_text_with_ocr(self, pdf_path):
        """Extract text using OCR for scanned PDFs."""
        text = ""
        images = convert_from_path(pdf_path)
        for image in images:
            text += pytesseract.image_to_string(image)
        return text