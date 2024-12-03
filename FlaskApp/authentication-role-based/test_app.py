import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def login(client, username, password):
    response = client.post('/login', json={"username": username, "password": password})
    return response.get_json().get("access_token") if response.status_code == 200 else None

def test_login_success(client):
    token = login(client, "admin_user", "admin123")
    assert token is not None

def test_login_failure(client):
    response = client.post('/login', json={"username": "wrong_user", "password": "wrong_pass"})
    assert response.status_code == 401
    assert response.get_json() == {"msg": "Invalid credentials"}

def test_view_resources(client):
    token = login(client, "tester_user", "tester123")
    response = client.get('/resources', headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_edit_resource_by_developer(client):
    token = login(client, "dev_user", "dev123")
    response = client.put('/resources/1', json={"name": "Updated Resource"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json()['name'] == "Updated Resource"

def test_edit_resource_by_tester(client):
    token = login(client, "tester_user", "tester123")
    response = client.put('/resources/1', json={"name": "Updated Resource"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
    assert response.get_json() == {"msg": "Permission denied"}

def test_delete_resource_by_admin(client):
    token = login(client, "admin_user", "admin123")
    response = client.delete('/resources/1', headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json() == {"msg": "Resource deleted"}

def test_delete_resource_by_developer(client):
    token = login(client, "dev_user", "dev123")
    response = client.delete('/resources/1', headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
    assert response.get_json() == {"msg": "Permission denied"}

def test_add_resource_by_admin(client):
    token = login(client, "admin_user", "admin123")
    response = client.post('/resources', json={"name": "New Resource", "description": "Admin added"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.get_json()['name'] == "New Resource"
