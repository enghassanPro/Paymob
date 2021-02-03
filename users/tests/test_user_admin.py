from rest_framework.test import APITestCase
from users.models.user import User
from knox.models import AuthToken
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK


class UserAdminTest(APITestCase):
    '''
        This Class use for test user process
        - test user admin can add new user
        - test user admin can retrieve all users
    '''
    def setUp(self) -> None:
        '''
            create user admin test and create token for this user
        '''
        self.user = User.objects.create_superuser("test", "test@test.com", "django123", type_account=1)
        _, self.token = AuthToken.objects.create(self.user)

        self.user_authenticate()

    def user_authenticate(self):
        '''
            prepare authentication to user admin to access any url in the system
        '''
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_authenticate(self):
        '''
            test authentication process
        '''
        self.client.force_authenticate(user=None)
        response = self.client.get("/admin/user/retrieve")
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_users(self):
        '''
            test retrieve users with user admin creds
        '''
        response = self.client.get("/admin/user/retrieve")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_add_user(self):
        '''
            test create client user with user admin creds
        '''
        data = {
            "username": "test_user",
            "first_name": "test",
            "last_name": "test",
            "phone": "0123",
            "address": "test address",
            "email": "test_user@test.com",
            "password": "django123"
        }
        response = self.client.post("/admin/user/create", data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_add_user_promo(self):
        '''
            test create client user with promo with user admin creds
        '''
        data = {
            "username": "test_user",
            "first_name": "test",
            "last_name": "test",
            "phone": "0123",
            "address": "test address",
            "email": "test_user@test.com",
            "password": "django123",
            "promo_type": "promo3",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "test description"
        }
        response = self.client.post("/admin/user/create", data)
        self.assertEqual(response.status_code, HTTP_200_OK)
