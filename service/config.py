"""
Global Configuration for the application
"""
import os

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)

SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv("SECRET_KEY", "sup3r-s3cr3t")
LOGGING_LEVEL = 20  # logging.INFO