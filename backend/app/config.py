from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "TrendPulse"
    debug: bool = True
    github_token: Optional[str] = None
    github_api_url: str = "https://api.github.com"
    database_url: str = "sqlite:///./trendpulse.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
