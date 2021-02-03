from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED
from users.serializers.promo.promoSerializer import ListPromoUserSerializer
from users.models.promo import Promo
from django.utils.timezone import now


class ClientAPIView(GenericAPIView):
    '''
        This class use for handle all possible process to the normal user
        In this class the normal user can do the following:
         - can retrieve either all valid promo that specify with it or retrieve a specific promo
            as you needed.

         - can take a promo code that specified for him.

    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
            @url: user/retrieve | user/retrieve?id=number
            @request: get
            @return: Array
        '''
        # check the type of request
        if kwargs['type'] == 'retrieve':
            # check the in query params.
            # then user specified a promo
            if "id" in self.request.query_params:
                try:
                    # validate the id that coming from query params if number
                    promo_id = int(self.request.query_params['id'])

                    # filter promo specified by id
                    promo = Promo.objects.filter(user_id=request.user.id,
                                                 id=promo_id,
                                                 is_active=True,
                                                 end_time__gte=now(),
                                                 start_time__lte=now())

                    # check exist or not
                    if promo.exists():
                        return Response(ListPromoUserSerializer(promo, many=True).data)

                    return Response({"error": "A promo with that id not found!"}, status=HTTP_400_BAD_REQUEST)

                except:

                    return Response({"error": "Invalid passing the parameters"}, status=HTTP_400_BAD_REQUEST)

            # otherwise user need to retrieve all promo that specified for him
            promos = Promo.objects.filter(user_id=request.user.id,
                                          is_active=True,
                                          end_time__gte=now(),
                                          start_time__lte=now())
            if promos.exists():

                return Response(ListPromoUserSerializer(promos, many=True).data)

            return Response({"error": "You haven't any Promo"}, status=HTTP_400_BAD_REQUEST)

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, *args, **kwargs):
        '''
            @url: user/submit?id=number
            @request: put
            @return: str
        '''
        if kwargs['type'] == 'submit':
            if {"id"} <= self.request.query_params.keys():

                try:
                    promo_id = int(self.request.query_params['id'])
                    promo = Promo.objects.filter(id=promo_id, is_active=True)

                    if promo.exists():
                        promo.update(is_active=False)
                        return Response("Successfully updated")

                    return Response({"error": "A promo with that id not found!"}, status=HTTP_400_BAD_REQUEST)

                except:
                    pass

            return Response({"error": "Invalid passing the parameters"}, status=HTTP_400_BAD_REQUEST)

        return Response({"detail": "Method Not Allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)
