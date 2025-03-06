from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://root:example@mongodb:27017/speechbot?authSource=admin"
    JWT_SECRET: str = "your_jwt_secret_key"

    class Config:
        env_file = ".env"

settings = Settings()
