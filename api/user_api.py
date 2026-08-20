import uuid

import requests


class UserApi:
    BASE_URL = "https://qa-stellarburgers.education-services.ru/api"

    def create_user(self):
        unique_id = uuid.uuid4().hex[:8]

        user = {
            "name": f"TestUser_{unique_id}",
            "email": f"test_{unique_id}@example.com",
            "password": f"Password_{unique_id}",
        }

        response = requests.post(
            f"{self.BASE_URL}/auth/register",
            json=user,
        )
        response.raise_for_status()

        data = response.json()

        return {
            "name": user["name"],
            "email": user["email"],
            "password": user["password"],
            "access_token": data["accessToken"],
            "refresh_token": data["refreshToken"],
        }

    def login(self, email, password):
        response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password,
            },
        )
        response.raise_for_status()

        return response.json()

    def get_user(self, access_token):
        response = requests.get(
            f"{self.BASE_URL}/auth/user",
            headers={
                "Authorization": access_token,
            },
        )
        response.raise_for_status()

        return response.json()

    def logout(self, refresh_token):
        response = requests.post(
            f"{self.BASE_URL}/auth/logout",
            json={
                "token": refresh_token,
            },
        )
        response.raise_for_status()

    def delete_user(self, access_token):
        response = requests.delete(
            f"{self.BASE_URL}/auth/user",
            headers={
                "Authorization": access_token,
            },
        )
        response.raise_for_status()

    def request_password_reset(self, email):
        response = requests.post(
            f"{self.BASE_URL}/password-reset",
            json={
                "email": email,
            },
        )
        response.raise_for_status()

        return response.json()