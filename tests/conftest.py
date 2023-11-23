import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, drop_database
from src.db import Base

"""使用していないが、後で確認する"""
@pytest.fixture(scope="session")
def testing_db_session():
    """テスト用DBセッション"""
    TEST_DATABASE_URL = "postgresql://postgres-test:password@postgres-db-test:5432/postgres"
    engine = create_engine(url=TEST_DATABASE_URL, echo=False, pool_recycle=10)
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, expire_on_commit=False, bind=engine)
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
