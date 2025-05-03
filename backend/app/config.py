import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "TriAid+ Backend"
    API_V1_STR: str = "/api/v1"

    DB_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost/triaid")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost")

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ALLOWED_ORIGINS = ["*"]

settings = Settings()
