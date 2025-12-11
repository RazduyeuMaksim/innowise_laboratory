from typing import Generator
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Path to the SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# SQLAlchemy Engine instance — manages DB connections
engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
    pool_pre_ping=True,
)

# Returns Session objects for transactional work
SessionLocal: sessionmaker[Session] = sessionmaker(
    autoflush=False, autocommit=False, bind=engine, class_=Session
)

# Declarative base class for ORM models.
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Creates a session, yields it, and closes it after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
