# core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fastapi-trainglo"
    secret_key: str
    debug: bool = False

    class Config:
        env_file = "a.env"


settings = Settings()
