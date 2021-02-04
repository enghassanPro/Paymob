from rest_framework.test import APITestCase
from users.serializers.admin.userSerializer import CreateUserSerializer


class UserAdminSerializerTestCase(APITestCase):
    '''
        This class use for test possible cases for validate user serializer
    '''

    def test_invalid_data_create(self):

        test = CreateUserSerializer(data={
            "email": "admin@admin.coms",
            "password": "django123"
        })
        if not test.is_valid():
            self.assertEqual(test.errors['username'], ["This field is required."])
