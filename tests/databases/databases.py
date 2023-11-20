from src.db import session_factory
from src.main import app
from tests.conftest import SessionLocal

def test_database(f):
    def setting_db(SessionLocal, *args, **kwargs):

        def override_get_db():
            session = SessionLocal()
            try:
                yield session
            finally:
                session.close()

        app.dependency_overrides[session_factory] = override_get_db
        # Run tests
        f(*args, **kwargs)
        # session_factoryを元に戻す
        app.dependency_overrides[session_factory] = session_factory
    return setting_db
