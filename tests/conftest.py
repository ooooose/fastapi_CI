import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import drop_database
from src.db import Base

@pytest.fixture(scope="function")
def SessionLocal():
    TEST_DATABASE_URL = "postgresql://postgres:password@postgres-db:5433/postgres"
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)

    session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield session_factory

    # Drop the test database
    drop_database(TEST_DATABASE_URL)

