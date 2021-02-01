from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from users.serializers.admin.userSerializer import CreateUserSerializer, ListUserSerializer
from users.models.user import User


class UserAPIView(GenericAPIView):
    '''
        This class use for user admin that can add or get users
    '''
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def get(self, request, *args, **kwargs):
        '''
            @url: admin/user/retrieve
            @request: get
            @return: Array
        '''
        if kwargs['type'] == 'retrieve':
            return Response(ListUserSerializer(User.objects.all(), many=True).data)

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        '''
            @url: admin/user/create
            @request data: {new user data} | {new user data & new promo data}
            @request: post
            @return: str
        '''
        if kwargs['type'] == 'create':

            create = CreateUserSerializer(data=self.request.data)
            create.is_valid(raise_exception=True)
            create.save()

            return Response("Successfully created")

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)
