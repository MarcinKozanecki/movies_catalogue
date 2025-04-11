from main import app
from unittest.mock import Mock
import pytest

@pytest.mark.parametrize('list_type', ['popular', 'top_rated', 'now_playing'])
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    
    monkeypatch.setattr("tmdb_client.get_movies_list", api_mock)
    
    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        
        assert response.status_code == 200
        
        api_mock.assert_called_once_with(list_type)
