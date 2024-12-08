def test_create_user(client):
    response = client.post("/users/", json={"username": "newuser", "password": "newpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"

