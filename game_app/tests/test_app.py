import pytest
from game_app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_scores_empty(client):
    response = client.get('/scores')
    assert response.status_code == 200
    assert response.json == []

def test_add_score(client):
    response = client.post('/scores', json={'player': 'Alice', 'score': 100})
    assert response.status_code == 200
    assert response.json['message'] == 'Score for Alice added successfully.'

def test_get_scores_with_data(client):
    client.post('/scores', json={'player': 'Alice', 'score': 100})
    client.post('/scores', json={'player': 'Bob', 'score': 150})
    response = client.get('/scores')
    assert response.status_code == 200
    assert response.json == [["Bob", 150], ["Alice", 100]]