"""Application configuration loaded from environment variables."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    cohere_api_key: str = ""
    source_url: str = ""
    embedding_model: str = "embed-english-v3.0"
    cohere_model: str = "command-a-03-2025"
    chunk_size: int = 1200
    chunk_overlap: int = 200
    retrieval_k: int = 10
    chroma_persist_directory: Path = Path("data/chroma")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
