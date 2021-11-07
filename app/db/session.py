from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
    # required for sqlite
    dbapi_connect_args = {"check_same_thread": False}
else:
    dbapi_connect_args = {}

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args=dbapi_connect_args,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
