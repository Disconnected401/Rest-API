import pytest
from API import app, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_users():
    users.clear()

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == []

def test_create_user(client):
    response = client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    assert response.status_code == 201
    assert response.json["name"] == "Wojciech"

def test_get_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json["id"] == 1

def test_patch_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.patch('/users/1', json={"name": "Jan"})
    assert response.status_code == 204

def test_put_user(client):
    response = client.put('/users/1', json={"name": "Anna", "lastname": "Nowak"})
    assert response.status_code == 204

def test_delete_user(client):
    client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    response = client.delete('/users/1')
    assert response.status_code == 204

def test_delete_user_nonexistent(client):
    response = client.delete('/users/999')
    assert response.status_code == 400

def test_create_user_missing_name(client):
    response = client.post('/users', json={"lastname": "Oczkowski"})
    assert response.status_code == 400

def test_create_user_missing_lastname(client):
    response = client.post('/users', json={"name": "Wojciech"})
    assert response.status_code == 400

def test_patch_user_nonexistent(client):
    response = client.patch('/users/999', json={"name": "Jan"})
    assert response.status_code == 400

def test_put_user_create_new(client):
    response = client.put('/users/1', json={"name": "Anna", "lastname": "Nowak"})
    assert response.status_code == 204
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json["name"] == "Anna"

if __name__ == "__main__":
    pytest.main()
