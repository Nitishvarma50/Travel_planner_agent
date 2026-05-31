import ymaml
import os

def load_config(config_path="config/config.yaml"):
    """
    Load the configuration from a YAML file
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    
    with open(config_path, "r") as f:
        config = ymaml.safe_load(f)
    
    return config