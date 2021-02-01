from rest_framework import serializers
from users.models.user import User


class UserLoginSerializer(serializers.ModelSerializer):
    '''
        This class use for validate the incoming data from login request
        The data should have email and password to check the user if already exists to continue process logging
        - validate and check the email and password if already valid
    '''

    email = serializers.EmailField(max_length=200, help_text="Enter email here", label="Email Address")
    password = serializers.CharField(help_text="Enter password here")
    error_msg = {
        "login": {"login": "Invalid Email or Password, Please try again!"},
    }

    class Meta:
        model = User
        fields = ('email', 'password',)

    def validate(self, attrs):

        # get user object of the incoming email to check if valid or not
        user = User.objects.filter(email__iexact=attrs['email'])

        if not user.exists():
            raise serializers.ValidationError(self.error_msg['login'])

        user = user.last()

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError(self.error_msg['login'])

        # store user object and return it to view
        attrs['client'] = user

        return attrs
