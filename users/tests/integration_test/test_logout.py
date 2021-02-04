from rest_framework.status import HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.test import APITestCase
from users.models.user import User
from knox.models import AuthToken


class LogoutTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser("test", "test@test.com", "django123", type_account=1)
        _, self.token = AuthToken.objects.create(self.user)

        self.user_authenticate()

    def user_authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_logout(self):

        response = self.client.get("/auth/logout")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_send_any_method_logout(self):

        response = self.client.post("/auth/logout")
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)
