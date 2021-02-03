from rest_framework.test import APITestCase
from users.models.user import User
from knox.models import AuthToken
from rest_framework.status import HTTP_200_OK


class PromoAdminTest(APITestCase):
    '''
        This Class use for test promo process with user admin creds
        - test user admin that can add new promo for specific user
        - test user admin that can retrieve all promos
        - test user admin that can update specific promo
        - test user admin that can delete specific promo
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

    def test_get_all_promo(self):
        '''
            test get all promo with user admin creds
        '''
        response = self.client.get("/admin/promo/retrieve")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_create_promo(self):
        '''
            test create promo for specific user with user admin creds
        '''
        data = {
            "user": 2,
            "promo_type": "promo",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "test description"
        }
        response = self.client.post("/admin/promo/create", data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def create_promo(self):
        data = {
            "user": 2,
            "promo_type": "promo",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "test description"
        }
        self.client.post("/admin/promo/create", data)

    def test_update_promo(self):
        '''
            test update promo for specific user with user admin creds
        '''
        self.create_promo()

        data = {
            "user": 2,
            "promo_type": "promo",
            "start_time": "2021-05-01T15:51:32.339118Z",
            "end_time": "2021-05-01T15:51:32.339118Z",
            "promo_amount": 38.5,
            "description": "tests description"
        }

        response = self.client.put("/admin/promo/update?id=1", data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_delete_promo(self):
        '''
            test delete promo for specific user with user admin creds
        '''
        self.create_promo()
        response = self.client.delete("/admin/promo/delete?id=1")
        self.assertEqual(response.status_code, HTTP_200_OK)
