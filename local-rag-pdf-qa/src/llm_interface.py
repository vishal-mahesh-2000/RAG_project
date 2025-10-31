"""Interface for Ollama LLM."""

import requests

class OllamaInterface:
    def __init__(self, config):
        self.base_url = config.get('ollama_url', 'http://localhost:11434')
        self.model = config.get('model', 'llama2')
    
    def generate(self, prompt, context=None):
        """Generate response from Ollama."""
        url = f"{self.base_url}/api/generate"
        data = {
            "model": self.model,
            "prompt": prompt,
            "context": context if context else []
        }
        
        response = requests.post(url, json=data)
        return response.json().get('response', '')