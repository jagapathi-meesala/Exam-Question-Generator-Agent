import os

class ConfigurationError(RuntimeError):
    pass

def required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ConfigurationError(f"required environment variable is missing: {name}")
    return value
