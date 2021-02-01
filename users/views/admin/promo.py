from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED
from users.serializers.promo.promoSerializer import (
    CreatePromoSerializer, ListUsersPromoSerializer,
    UpdatePromoSerializer
)
from users.models.promo import Promo
from django.utils.timezone import now


class PromoAPIView(GenericAPIView):
    '''
        This class for user admin only to create a new promo or update or delete for specific user
        and retrieve all promo of all users
    '''
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def get(self, request, *args, **kwargs):
        '''
            @url: admin/promo/retrieve
            @request: get
            @return: Array
        '''
        if kwargs['type'] == 'retrieve':
            return Response(ListUsersPromoSerializer(Promo.objects.filter(end_time__gte=now()), many=True).data)

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        '''
            @url: admin/promo/create
            @request data: {new promo data}
            @request: post
            @return: str
        '''
        if kwargs['type'] == 'create':

            promo = CreatePromoSerializer(data=self.request.data)
            promo.is_valid(raise_exception=True)
            promo.save()

            return Response("Successfully created")

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, *args, **kwargs):
        '''
            @url: admin/promo/update?id=number
            @request data: {update promo data}
            @request: put
            @return: str
        '''
        if kwargs['type'] == 'update':
            if {"id"} <= self.request.query_params.keys():

                try:
                    promo_id = int(self.request.query_params['id'])

                except:
                    return Response({"error": "Invalid passing the parameters"}, status=HTTP_400_BAD_REQUEST)

                promo = Promo.objects.filter(id=promo_id)

                if promo.exists():
                    promo = UpdatePromoSerializer(promo.last(), data=self.request.data)
                    promo.is_valid(raise_exception=True)
                    promo.save()
                    return Response("successfully updated")

                return Response({"error": "A promo with that id not found!"}, status=HTTP_400_BAD_REQUEST)

            return Response({"error": "Invalid passing the parameters"}, status=HTTP_400_BAD_REQUEST)

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        '''
            @url: admin/promo/delete?id=number
            @request: delete
            @return: str
        '''
        if kwargs['type'] == 'delete':
            if {"id"} <= self.request.query_params.keys():

                try:
                    promo_id = int(self.request.query_params['id'])

                except:
                    return Response({"error": "Invalid passing the parameters"}, status=HTTP_400_BAD_REQUEST)

                promo = Promo.objects.filter(id=promo_id)

                if promo.exists():
                    promo.delete()
                    return Response("successfully deleted")

                return Response({"error": "A promo with that id not found!"}, status=HTTP_400_BAD_REQUEST)

            return Response({"error": "Invalid passing the parameters"}, status=HTTP_400_BAD_REQUEST)

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)