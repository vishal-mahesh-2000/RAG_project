"""Tests for vector store."""

import pytest
import numpy as np
from src.vector_store import VectorStore
from src.config import Config
import os

@pytest.fixture
def config():
    return Config("config/config.json")

@pytest.fixture
def vector_store(config):
    return VectorStore(config)

def test_add_and_search(vector_store):
    docs = ["doc1", "doc2", "doc3"]
    embeddings = np.random.rand(3, 128)
    vector_store.add_documents(docs, embeddings)
    
    query_embedding = np.random.rand(128)
    results = vector_store.search(query_embedding, k=2)
    
    assert len(results) == 2
    assert all(isinstance(doc, str) and isinstance(dist, float) for doc, dist in results)

def test_save_and_load(vector_store, tmp_path):
    docs = ["doc1", "doc2"]
    embeddings = np.random.rand(2, 128)
    vector_store.add_documents(docs, embeddings)
    
    save_path = str(tmp_path)
    vector_store.save(save_path)
    
    new_store = VectorStore(Config("config/config.json"))
    new_store.load(save_path)
    
    assert len(new_store.documents) == len(docs)