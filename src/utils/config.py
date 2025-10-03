"""
Configuration Module
Handles application configuration
"""

import os


class Config:
    """Configuration management"""
    
    def __init__(self):
        self.settings = {
            'request_delay': float(os.getenv('CRAWL_DELAY', '1.0')),
            'max_pages': int(os.getenv('MAX_PAGES', '100')),
            'ai_enabled': os.getenv('AI_ENABLED', 'true').lower() == 'true',
            'output_format': os.getenv('OUTPUT_FORMAT', 'json')
        }
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        self.settings[key] = value
