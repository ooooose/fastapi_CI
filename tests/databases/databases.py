from src.db import session_maker
from src.main import app

def test_database(f):
    def setting_db(SessionLocal, *args, **kwargs):

        def override_get_db():
            session = SessionLocal()
            try:
                yield session
            finally:
                session.close()

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[session_maker] = override_get_db
        # Run tests
        f(*args, **kwargs)
        # get_dbを元に戻す
        app.dependency_overrides[session_maker] = get_db
    return setting_db
