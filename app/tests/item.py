from fastapi import status

def test_create_item(test_app):
    response = test_app.post("/items/", json={"name": "Test Item"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "Test Item"
    assert "id" in response.json()