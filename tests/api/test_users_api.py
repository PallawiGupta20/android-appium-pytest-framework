import pytest
from tests.api.api_client import ApiClient

client = ApiClient()


def test_get_user_success():
    response = client.get_user(2)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["id"] == 2
    assert "email" in data


def test_get_user_not_found():
    response = client.get_user(9999)
    assert response.status_code == 404


def test_create_user():
    response = client.create_user("Pallawi", "QA Automation Engineer")
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Pallawi"
    assert data["job"] == "QA Automation Engineer"


def test_update_user():
    response = client.update_user(2, "Pallawi Gupta", "Senior QA Engineer")
    assert response.status_code == 200
    assert response.json()["job"] == "Senior QA Engineer"


def test_delete_user():
    response = client.delete_user(2)
    assert response.status_code == 204


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_multiple_users(user_id):
    response = client.get_user(user_id)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


def test_response_time_is_acceptable():
    response = client.get_user(2)
    assert response.elapsed.total_seconds() < 2.0
