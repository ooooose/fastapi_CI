import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, drop_database
from src.db import Base

@pytest.fixture(scope="function")
def SessionLocal():
    # TODO: URLが合っているか確認
    TEST_DATABASE_URL = "postgresql://postgres-test:password@postgres-db-test:5432/postgres"
    engine = create_engine(TEST_DATABASE_URL)

    Base.metadata.create_all(engine)

    session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # Run the tests
    session = session_factory()
    yield session
    session.close()

    # Drop the test database
    drop_database(TEST_DATABASE_URL)


