"""Utility functions."""

import logging
import os

def setup_logging(log_dir):
    """Set up logging configuration."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(log_dir, 'app.log')),
            logging.StreamHandler()
        ]
    )
    
def ensure_directory(directory):
    """Ensure a directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)