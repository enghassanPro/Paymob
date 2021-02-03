from rest_framework.test import APITestCase
from users.models.user import User
from users.models.promo import Promo
from knox.models import AuthToken
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_400_BAD_REQUEST


class PromoPerUserTest(APITestCase):
    '''
        This Class use for test promo process with client creds
        - test client user that can retrieve all specified promos
        - test client user that can retrieve a specific promos
        - test client user that can take specific promo
        - test client user that can delete specific promo
    '''
    def setUp(self) -> None:
        '''
           create client user test and create token for this user
       '''
        data = {
            "username": "test_user",
            "first_name": "test",
            "last_name": "test",
            "phone": "0123",
            "address": "test address",
            "email": "test_user@test.com",
            "password": "django123",
            "type_account": 2,
        }
        self.user = User.objects.create(**data)

        data = {
            "user_id": 2,
            "promo_type": "promo3",
            "start_time": "2021-02-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "testtstststtsts"
        }

        self.promo = Promo.objects.create(**data)

        _, self.token = AuthToken.objects.create(self.user)

        self.user_authenticate()

    def user_authenticate(self):
        '''
            prepare authentication to client user to access specified url
        '''
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_add_promo_user(self):
        '''
            test create new promo with client user creds
        '''
        data = {
            "user": 2,
            "promo_type": "promo",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "testtstststtsts"
        }
        response = self.client.post("/admin/promo/create", data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def create_promo(self):
        data = {
            "user": 2,
            "promo_type": "promo",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "testtstststtsts"
        }
        self.client.post("/admin/promo/create", data)

    def test_update_promo_user(self):
        '''
            test update for any promo with client user creds
        '''
        self.create_promo()
        data = {
            "user": 2,
            "promo_type": "promo",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "testtstststtsts"
        }
        response = self.client.put("/admin/promo/update?id=1", data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_delete_promo_user(self):
        '''
            test delete any promo with client user creds
        '''
        self.create_promo()

        response = self.client.delete("/admin/promo/update?id=1")
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_promo_not_current_user_or_not_found(self):
        '''
            test get specified promos with client user creds
        '''
        response = self.client.get("/user/retrieve?id=10")
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_get_all_promo_per_user(self):
        '''
            test get all specified promos with client user creds
        '''
        response = self.client.get("/user/retrieve")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_promo_per_user(self):
        '''
            test get a specific promo with client user creds
        '''
        response = self.client.get("/user/retrieve?id=1")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_take_promo(self):
        '''
            test take a specific promo with client user creds
        '''
        response = self.client.put("/user/submit?id=1")
        self.assertEqual(response.status_code, HTTP_200_OK)
