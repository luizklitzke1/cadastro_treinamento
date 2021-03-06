import pytest
from backend import create_app

@pytest.fixture(scope="module")
def app():
    app=create_app(testing=True)
    yield app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()