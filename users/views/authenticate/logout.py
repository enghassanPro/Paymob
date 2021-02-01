from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class UserLogoutView(RetrieveAPIView):
    '''
        This class use for destory the session and token for this user and logout from the system
    '''
    # check permission for each user if authenticated or not
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
            @url: auth/logout
            @request: get
            @return: str
        '''

        # delete token
        self.request._auth.delete()

        # destory all stored data about this user
        logout(self.request)

        return Response("successfully logged out")

