import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///test.db")