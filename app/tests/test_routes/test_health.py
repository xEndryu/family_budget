def test_health(client):
    response = client.get("api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"
