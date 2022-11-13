from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOST_DB = "db-pg"
PORT = 5432
POSTGRES_USER="admin"
POSTGRES_PASSWORD="admin"
POSTGRES_DB="rainbow_database"


SQLALCHEMY_DATABASE_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST_DB}:5432/{POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative_base()
