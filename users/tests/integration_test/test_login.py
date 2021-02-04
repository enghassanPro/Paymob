from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase


class LoginTestCase(APITestCase):

    def test_login(self):

        data = {
            "email": "admin@admin.com",
            "password": "django123"
        }

        response = self.client.post("/auth/login", data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_invalid_creds(self):
        data = {
            "email": "admin@admin.com",
            "password": "django1234"
        }

        response = self.client.post("/auth/login", data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)