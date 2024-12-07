from dotenv import load_dotenv
import os

load_dotenv()  # Wczytaj zmienne z pliku .env


class Config:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "discoelysium")
    DB_NAME = os.getenv("DB_NAME", "datadepot_db")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

