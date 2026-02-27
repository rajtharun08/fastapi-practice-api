import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Enterprise Asset Management System"
    DATABASE_URL: str = os.getenv("DATABASE_URL","postgresql://postgres:Tharun%4008@localhost:5432/eams_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()