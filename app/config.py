import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "BBC News API")
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    CONNSTR: str = os.getenv("CONNSTR", "")
    POSTGRES_SCHEMA: str = os.getenv("POSTGRES_SCHEMA", "temporary_data")
    POSTGRES_TABLE: str = os.getenv("POSTGRES_TABLE", "silver_bbc_useful_news")


settings = Settings()