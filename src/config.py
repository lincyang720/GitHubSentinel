import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///sentinel.db")
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", "86400"))  # 秒
