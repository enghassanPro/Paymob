from rest_framework import serializers
from users.models.promo import Promo


class CreatePromoSerializer(serializers.ModelSerializer):
    '''
        This Class use for Create a new Promo.
        Should have all fields in the data to create the new record
        will validate all data with the default and custom validation that already setup into the model class
    '''
    class Meta:
        model = Promo
        fields = "__all__"


class UpdatePromoSerializer(serializers.ModelSerializer):
    '''
        This Class use for update the exist Promo.
        Should have all fields in the data to update the record
        will validate all data with the default and custom validation that already setup into the model class
    '''
    class Meta:
        model = Promo
        fields = "__all__"


class ListUsersPromoSerializer(serializers.ModelSerializer):

    '''
        This Class use for retrieve all Promo that stored into the database.
    '''

    class Meta:
        model = Promo
        fields = "__all__"

    def to_representation(self, instance):
        '''
            This function use for customize the retrieve data from the model
            - change all dates to a custom format
            - retrieve all data of user and add it to user object
        '''
        represented = super().to_representation(instance)
        represented['created'] = instance.created.strftime("%a %b %y %H:%M %p")
        represented['start_time'] = instance.start_time.strftime("%a %b %y %H:%M %p")
        represented['end_time'] = instance.end_time.strftime("%a %b %y %H:%M %p")

        represented['user'] = {
            "id": instance.user.id,
            "full_name": instance.user.get_full_name(),
            "type_account": instance.user.get_type_account(),
            "phone": instance.user.phone,
            "email": instance.user.email,
            "date_joined": instance.user.date_joined.strftime("%a %b %y %H:%M %p")
        }

        return represented


class ListPromoUserSerializer(serializers.ModelSerializer):

    '''
        This Class use for retrieve a Promo that specify with id.
    '''
    class Meta:
        model = Promo
        fields = "__all__"
