# tests/test_user.py
from fastapi import status

def test_create_user(test_app):
    response = test_app.post("/users/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "testuser"
    assert "id" in response.json()