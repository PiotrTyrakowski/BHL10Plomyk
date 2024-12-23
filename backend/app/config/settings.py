from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./space_app.db"
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    redis_url: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"

settings = Settings()

