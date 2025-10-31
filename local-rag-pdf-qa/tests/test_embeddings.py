"""Tests for embeddings generation."""

import pytest
import numpy as np
from src.embeddings import EmbeddingsGenerator
from src.config import Config

@pytest.fixture
def config():
    return Config("config/config.json")

@pytest.fixture
def embeddings_generator(config):
    return EmbeddingsGenerator(config)

def test_generate_embeddings(embeddings_generator):
    text = "This is a test sentence."
    embeddings = embeddings_generator.generate(text)
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.ndim == 1
    assert embeddings.shape[0] > 0