"""Vector store implementation using FAISS."""

import faiss
import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, config):
        self.config = config
        self.index = None
        self.documents = []
        
    def add_documents(self, documents, embeddings):
        """Add documents and their embeddings to the store."""
        if self.index is None:
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.documents.extend(documents)
    
    def search(self, query_embedding, k=5):
        """Search for similar documents."""
        distances, indices = self.index.search(query_embedding.reshape(1, -1), k)
        return [(self.documents[i], distances[0][i]) for i in indices[0]]
    
    def save(self, path):
        """Save the vector store to disk."""
        faiss.write_index(self.index, os.path.join(path, "index.faiss"))
        with open(os.path.join(path, "documents.pkl"), "wb") as f:
            pickle.dump(self.documents, f)
    
    def load(self, path):
        """Load the vector store from disk."""
        self.index = faiss.read_index(os.path.join(path, "index.faiss"))
        with open(os.path.join(path, "documents.pkl"), "rb") as f:
            self.documents = pickle.load(f)