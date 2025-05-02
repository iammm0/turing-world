from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int

    # Qdrant
    QDRANT_HOST: str
    QDRANT_PORT: int

    # OpenAI / LLM
    OPENAI_API_KEY: str
    OPENAI_API_BASE: str
    DEFAULT_LLM_PROVIDER: str
    DEFAULT_AI_MODEL: str

    # JWT & Security
    JWT_SECRET: str
    JWT_ALGORITHM: str

    # Other
    PROJECT_NAME: str = "turing-world"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()