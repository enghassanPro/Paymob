from rest_framework import serializers
from users.models.user import User
from users.models.promo import Promo


class CreateUserSerializer(serializers.ModelSerializer):
    '''
        This class use for create new normal user
        The user admin have 2 options:

        - The user admin can add user and promo
        - The user admin can add user only
    '''
    promo_type = serializers.CharField(required=False)
    start_time = serializers.DateTimeField(required=False)
    end_time = serializers.DateTimeField(required=False)
    promo_amount = serializers.FloatField(required=False)
    description = serializers.CharField(required=False)

    # store all required promo data to create it
    promo_data = ['promo_type', 'start_time', 'end_time', 'promo_amount', 'description']

    error_msg = {
        "promo": {"promo_data": "Please add all data promo, or you can leave them!"}

    }

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password', 'address',
                  'promo_type', 'start_time', 'end_time', 'promo_amount', 'description',)

    def validate(self, attrs):

        # check if the user admin add any field of promo data to validate for all data of promo
        for dt in self.promo_data:
            if dt in attrs and attrs[dt] is None or '':
                raise serializers.ValidationError(self.error_msg['promo'])

        return attrs

    def create(self, validated_data):

        # create and store the new user
        user = User(username=validated_data['username'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    email=validated_data['email'],
                    phone=validated_data['phone'],
                    address=validated_data['address'],
                    type_account=2)

        # set password hash
        user.set_password(validated_data['password'])
        user.save()

        # if the user admin add the of promo model then will be create
        if self.promo_data[0] in validated_data:
            Promo(user=user, **{k: validated_data[k] for k in self.promo_data}).save()

        return user


class ListUserSerializer(serializers.ModelSerializer):
    '''
        This class use for retrieve all users that stored in the system
    '''
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'date_joined')

    def to_representation(self, instance):
        represented = super().to_representation(instance)

        # return string of type account
        represented['type_account'] = instance.get_type_account()

        return represented
