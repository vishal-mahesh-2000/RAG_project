"""Embeddings generation module using sentence-transformers."""

from sentence_transformers import SentenceTransformer

class EmbeddingsGenerator:
    def __init__(self, config):
        self.model = SentenceTransformer(config.get('embedding_model', 'all-MiniLM-L6-v2'))
    
    def generate(self, text):
        """Generate embeddings for the given text."""
        return self.model.encode(text)