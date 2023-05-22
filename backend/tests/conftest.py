import sys
sys.path.append("..")
from src.app import create_app
import pytest

@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

