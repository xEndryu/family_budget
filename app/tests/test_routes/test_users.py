user_dict = {"username": "testuser", "email": "testuser@nofoobar.com", "password": "testing"}


def test_create_user(client):
    response = client.post("/api/v1/users", json=user_dict)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] is True


def test_duplicated_email(client):
    client.post("/api/v1/users", json=user_dict)
    user = {"username": "testuser2", "email": "testuser@nofoobar.com", "password": "testing"}
    response = client.post("/api/v1/users", json=user)
    assert response.status_code == 400
    assert response.json()["detail"] == 'Email already registered'


def test_duplicated_username(client):
    client.post("/api/v1/users", json=user_dict)
    user = {"username": "testuser", "email": "testuser2@nofoobar.com", "password": "testing"}
    response = client.post("/api/v1/users", json=user)
    assert response.status_code == 400
    assert response.json()["detail"] == 'Username already registered'
