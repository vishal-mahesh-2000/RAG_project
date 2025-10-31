"""Configuration management module."""

import json
import os
from dotenv import load_dotenv

class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self._load_config()
        load_dotenv()
        
    def _load_config(self):
        """Load configuration from JSON file."""
        with open(self.config_path) as f:
            return json.load(f)
    
    def get(self, key, default=None):
        """Get configuration value."""
        return self.config.get(key, default)
    
    def get_env(self, key, default=None):
        """Get environment variable."""
        return os.getenv(key, default)