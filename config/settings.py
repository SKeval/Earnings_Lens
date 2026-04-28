from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(env_file=".env")
    
    HUGGINGFACE_API_KEY: str
    SUPABASE_KEY: str
    SUPABASE_URL: str
    REDIS_URL: str = Field(default="redis://localhost:6379")
    ENV: str = Field(default="development")
    

settings = Settings()

if __name__ == "__main__":
    print(settings.model_dump())