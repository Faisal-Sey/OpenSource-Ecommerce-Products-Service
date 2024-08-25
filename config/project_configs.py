import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

PROJECT_CONFIGS = {
    "CUSTOM_CORS_ALLOWED_ORIGINS": os.getenv("CUSTOM_CORS_ALLOWED_ORIGINS"),
    "API_VERSION": os.getenv("API_VERSION"),
    "DEBUG": os.getenv("DEBUG"),
    "ALLOWED_HOST": os.getenv("ALLOWED_HOST"),
    "USE_EXTERNAL_LOGGER": os.getenv("USE_EXTERNAL_LOGGER"),
}


SORT_KEY_CHOICES = ("created_on", "price", "best_selling", "relevance")
