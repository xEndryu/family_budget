from fastapi import status


def test_create_budget(client, normal_user_token_headers):
    data = {
        "name": "AC budget",
        "description": "Money to buy an air conditioner",
        "amount": 100
    }
    response = client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "AC budget"
    assert response.json()["description"] == "Money to buy an air conditioner"
    assert response.json()["category"] == "incomes"


def test_create_budget_outcome(client, normal_user_token_headers):
    data = {
        "name": "AC budget",
        "description": "Money to buy an air conditioner",
        "amount": -200
    }
    response = client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "AC budget"
    assert response.json()["description"] == "Money to buy an air conditioner"
    assert response.json()["category"] == "outcomes"


def test_read_all_budgets_with_pagination(client, normal_user_token_headers):
    data = {
        "name": "AC budget",
        "description": "Money to buy an air conditioner",
        "amount": 100
    }
    client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)

    response = client.get("/api/v1/budgets/?page=1&size=50", headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["total"] == 2
    assert response.json()["page"] == 1
    assert response.json()["size"] == 50


def test_read_all_budgets_with_filter(client, normal_user_token_headers):
    data = {
        "name": "AC budget",
        "description": "Money to buy an air conditioner",
        "amount": -200
    }
    client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    data["amount"] == 100
    client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)

    response = client.get("/api/v1/budgets/?page=1&size=50&category=incomes", headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["items"][0]
    assert not response.json()["total"] == 1


def test_update_a_budget(client, normal_user_token_headers):
    data = {
        "name": "AC budget",
        "description": "Money to buy an air conditioner",
        "amount": 100
    }
    resp = client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    budget_id = resp.json()["id"]
    data["name"] = "Random budget"
    response = client.put(f"/api/v1/budgets/{budget_id}", json=data, headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["msg"] == "Successfully updated data"


def test_delete_a_budget(client, normal_user_token_headers):
    data = {
        "name": "AC budget",
        "description": "Money to buy an air conditioner",
        "amount": 100
    }
    response = client.post("/api/v1/budgets/", json=data, headers=normal_user_token_headers)
    budget_id = response.json()["id"]
    resp = client.delete(f"/api/v1/budgets/{budget_id}", headers=normal_user_token_headers)
    response = client.get(f"/api/v1/budgets/{budget_id}/", headers=normal_user_token_headers)
    assert resp.json()["msg"] == "Successfully deleted"
    assert response.status_code == status.HTTP_404_NOT_FOUND
