import logging
import os
import json
from typing import Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse config file: {e}")
        return {}

def get_environment_variable(var_name: str) -> str:
    try:
        return os.environ[var_name]
    except KeyError:
        logger.error(f"Environment variable {var_name} not set")
        return ""

def validate_config(config: Dict[str, Any]) -> bool:
    required_keys = ["server", "port", "secret_key"]
    for key in required_keys:
        if key not in config:
            logger.error(f"Missing required config key: {key}")
            return False
    return True

class ConfigLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config = load_config(file_path)

    def get_config(self) -> Dict[str, Any]:
        if not validate_config(self.config):
            raise ValueError("Invalid config")
        return self.config

    def reload_config(self):
        self.config = load_config(self.file_path)