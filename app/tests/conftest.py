# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the root directory of your project to sys.path
import sys
sys.path.append("c:/users/sankalp/django quantum/app")  # Replace with the actual path to your project's root directory

# Correct the import statement for the app module
from ..app.core.config import settings
from ..app.db import Base, engine


def override_get_db():
    testing_db = create_engine(settings.TEST_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=testing_db)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_app():
    # Use the same main.py but with a different database
    settings.TESTING = True
    # Reset the tables in the test database before running the tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    from main import app

    app.dependency_overrides[deps.get_db] = override_get_db
    yield TestClient(app)

