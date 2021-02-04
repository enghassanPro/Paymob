from rest_framework.test import APITestCase
from users.serializers.authenticate.loginSerializer import UserLoginSerializer


class LoginSerializerTestCase(APITestCase):
    '''
        This class use for test possible cases for validate login serializer
    '''

    def test_invalid_email(self):

        test = UserLoginSerializer(data={
            "email": "admin@admin.coms",
            "password": "django123"
        })
        if not test.is_valid():
            self.assertEqual(test.errors['login'], ["Invalid Email or Password, Please try again!"])

    def test_invalid_password(self):

        test = UserLoginSerializer(data={
            "email": "admin@admin.com",
            "password": "django1234"
        })
        if not test.is_valid():
            self.assertEqual(test.errors['login'], ["Invalid Email or Password, Please try again!"])

    def test_not_empty_password(self):

        test = UserLoginSerializer(data={
            "email": "admin@admin.com",
            "password": ""
        })
        if not test.is_valid():
            self.assertEqual(test.errors['password'], ["This field may not be blank."])

    def test_not_empty_email(self):
        test = UserLoginSerializer(data={
            "email": "",
            "password": "123"
        })
        if not test.is_valid():
            self.assertEqual(test.errors['email'], ["This field may not be blank."])

    def test_require_email(self):
        test = UserLoginSerializer(data={
            "password": "123"
        })
        if not test.is_valid():
            self.assertEqual(test.errors['email'], ["This field is required."])

    def test_require_password(self):
        test = UserLoginSerializer(data={
            "email": "123"
        })
        if not test.is_valid():
            self.assertEqual(test.errors['password'], ["This field is required."])
