import tmdb_client
import pytest
from unittest.mock import Mock

# Test get_single_movie
def test_get_single_movie(monkeypatch):
    mock_response = Mock()
    expected_result = {"id": 42, "title": "Test Movie"}

    mock_response.json.return_value = expected_result
    mock_response.status_code = 200
    monkeypatch.setattr("requests.get", lambda url: mock_response)

    movie = tmdb_client.get_single_movie(42)
    assert movie == expected_result

def test_get_single_movie_404(monkeypatch, capsys):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.text = "Not Found"
    mock_response.json.return_value = {}

    monkeypatch.setattr("requests.get", lambda url: mock_response)

    tmdb_client.get_single_movie(123)
    captured = capsys.readouterr()
    assert "Error fetching movie details" in captured.out

# Test get_movie_cast
def test_get_movie_cast(monkeypatch):
    mock_response = Mock()
    fake_cast = [{"name": "Actor 1"}, {"name": "Actor 2"}]
    mock_response.status_code = 200
    mock_response.json.return_value = {"cast": fake_cast}

    monkeypatch.setattr("requests.get", lambda url: mock_response)

    cast = tmdb_client.get_movie_cast(42)
    assert cast == fake_cast[:8]

def test_get_movie_cast_error(monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 404
    monkeypatch.setattr("requests.get", lambda url: mock_response)

    cast = tmdb_client.get_movie_cast(123)
    assert cast == []

# Jeśli chcesz przetestować get_movie_images (której jeszcze nie ma)
def test_get_movie_images(monkeypatch):
    mock_response = Mock()
    fake_images = {"backdrops": [{"file_path": "/abc.jpg"}]}
    mock_response.status_code = 200
    mock_response.json.return_value = fake_images

    monkeypatch.setattr("requests.get", lambda url: mock_response)

    # Zakładamy, że dodasz tę funkcję do tmdb_client.py
    images = tmdb_client.get_movie_images(42)
    assert images == fake_images
