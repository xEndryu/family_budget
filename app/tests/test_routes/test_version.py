def test_version(client):
    response = client.get("/ap1/v1/version")
    assert response.status_code == 200
    assert response.json().get('product') == "Family Budget"
    assert response.json().get('version') == "1.0.0"
    assert response.json().get('branch') is not None
    assert response.json().get('build_id') is not None
    assert response.json().get('build_date') is not None
    assert response.json().get('commit_hash') is not None
