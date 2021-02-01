from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from users.serializers.authenticate.loginSerializer import UserLoginSerializer
from django.contrib.auth import login
from django.utils.timezone import now
from knox.models import AuthToken
from knox.settings import knox_settings


class UserLoginView(CreateAPIView):
    '''
        This class will fire if the request is auth/login.
        This class use for login the users and generate token for each user
    '''

    # set serializer class
    serializer_class = UserLoginSerializer

    def get_token_ttl(self):
        # return The Token expire time
        return knox_settings.TOKEN_TTL

    def get_token_limit_per_user(self):
        # return The limit number of tokens per user
        return knox_settings.TOKEN_LIMIT_PER_USER

    def check_token_limit_per_user(self, request):
        # check the limit number of tokens per user if exceed or not
        # return True if not exceed
        # otherwise False
        token_limit_per_user = self.get_token_limit_per_user()

        if token_limit_per_user is not None:
            token = request.user.auth_token_set.filter(expiry__gt=now())
            if token.count() >= token_limit_per_user:
                return False

        return True

    def generate_token(self, user):
        # set time token expire and generate the token with knox framework.
        _, token = AuthToken.objects.create(user, self.get_token_ttl())

        return token

    def post(self, request, *args, **kwargs):
        '''
            @url: auth/login
            @request data: {email: str, password: str}
            @request: post
            @return: {token: str}
        '''
        # check if email and password in the data
        if {'email', 'password'} <= self.request.data.keys():
            # pass the data to serializer to make validate for these data
            user = self.serializer_class(data=self.request.data)

            # start validation and return error if happens
            user.is_valid(raise_exception=True)

            # get user object after success validate data
            user = user.validated_data['client']

            # check if this user is active
            if user.is_active:

                # check the limit token per user if exceed or not
                if not self.check_token_limit_per_user(request):
                    return Response({"error": [f"You Logged in from {self.get_token_limit_per_user()} devices!"]},
                                    status=HTTP_400_BAD_REQUEST)

                # store the user object
                login(request, user)

                # generate token and return it
                return Response({"token": self.generate_token(user)})

            return Response({"not_activate": [
                "This User isn't active please contact admin to activate your account!"]},
                            status=HTTP_400_BAD_REQUEST)

        return Response({"error": ["Error! Invalid passing the parameters"]}, status=HTTP_400_BAD_REQUEST)
