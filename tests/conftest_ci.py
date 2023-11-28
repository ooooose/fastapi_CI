from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db import Base


def override_session_factory():
    TEST_DATABASE_URL = (
        "postgresql://postgres-test:password@localhost:5432/postgres-test"
    )
    engine = create_engine(
        url=TEST_DATABASE_URL, echo=False, pool_recycle=10, isolation_level="AUTOCOMMIT"
    )
    SessionLocal = sessionmaker(
        autocommit=False, autoflush=True, expire_on_commit=False, bind=engine
    )

    Base.metadata.create_all(engine)

    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
