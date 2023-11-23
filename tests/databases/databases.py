from src.db import session_factory
from src.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# def test_database(f):
#     def setting_db(SessionLocal, *args, **kwargs):
#
#         def override_get_db():
#             session = SessionLocal()
#             try:
#                 yield session
#             finally:
#                 session.close()
#
#         app.dependency_overrides[session_factory] = override_get_db
#         # Run tests
#         f(*args, **kwargs)
#         # session_factoryを元に戻す
#         app.dependency_overrides[session_factory] = session_factory
#     return setting_db

def override_session_factory():
    TEST_DATABASE_URL = "postgresql://postgres:password@postgres-db:5432/postgres"
    engine = create_engine(url=TEST_DATABASE_URL, echo=False, pool_recycle=10, isolation_level="AUTOCOMMIT")
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, expire_on_commit=False, bind=engine)

    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
