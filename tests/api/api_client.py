import requests


class ApiClient:
    """Reusable API client - mirrors the Page Object pattern used in the UI tests."""

    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, name, job):
        return requests.post(f"{self.base_url}/users", json={"name": name, "job": job})

    def update_user(self, user_id, name, job):
        return requests.put(f"{self.base_url}/users/{user_id}", json={"name": name, "job": job})

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}")
