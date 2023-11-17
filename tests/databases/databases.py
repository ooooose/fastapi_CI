from src.db import session_factory
from src.main import app

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
        # get_dbを元に戻す
        app.dependency_overrides[session_factory] = get_db
    return setting_db
