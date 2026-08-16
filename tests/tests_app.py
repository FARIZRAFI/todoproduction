from unittest.mock import MagicMock, patch
import pytest
from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("app.app.get_db")
def test_index_route(mock_get_db, client):
    """Test the main index route GET request."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = mock_db
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {"id": 1, "title": "Test todo"}
    ]

    response = client.get("/")
    assert response.status_code == 200


@patch("app.app.get_db")
def test_add_todo_route(mock_get_db, client):
    """Test adding a todo item POST request."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = mock_db
    mock_db.cursor.return_value = mock_cursor

    response = client.post("/add", data={"title": "New Task"})
    assert response.status_code == 302
