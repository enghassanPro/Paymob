from rest_framework.test import APITestCase
from users.serializers.promo.promoSerializer import CreatePromoSerializer


class PromoAdminSerializerTestCase(APITestCase):
    '''
        This class use for test possible cases for validate promo serializer
    '''

    def test_invalid_data_create(self):

        test = CreatePromoSerializer(data={
        })
        if not test.is_valid():
            self.assertEqual(test.errors['user'], ["This field is required."])

    def test_not_empty_data_create(self):
        test = CreatePromoSerializer(data={
            "user": "",
            "promo_type": "",
            "start_time": "",
            "end_time": "",
            "promo_amount": "",
            "description": "",

        })
        if not test.is_valid():
            self.assertEqual(test.errors['user'], ["This field may not be null."])