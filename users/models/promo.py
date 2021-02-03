from django.db import models
from django.utils.translation import gettext_lazy as _
from .user import User
from django.core.validators import RegexValidator
import uuid
from random import shuffle, randint


def generate_promo_code():
    '''
        This function will fire every record that will be store.
        It used to generate a promo code
    '''

    while True:
        arr = str(uuid.uuid4()).split('-')
        shuffle(arr)
        if len(arr) > 3:
            res = ''.join(arr[randint(0, len(arr)-1)])
            return res[:7] if len(res) >= 7 else res


class Promo(models.Model):
    '''
        This class model stores all possible data of the Promo process
        The structure of the model is:
        - each user should have a list of promo codes.
        - we make a relation One To many between the user model and this model.
        - each promo should have one user and each user should have a list of promo

    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    promo_type = models.CharField(max_length=100,
                                  help_text=_('Required. 100 characters or fewer. Letters and numbers only.'),
                                  validators=[RegexValidator(regex="^[a-zA-Z0-9]{4,100}$",
                                              message="Enter a valid promo type. Minimum 4 characters and should be contains letters and numbers only")],
                                  )

    promo_code = models.CharField(max_length=300, unique=True,
                                  default=generate_promo_code,
                                  editable=False)

    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    promo_amount = models.FloatField()
    is_active = models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        # set name of the table
        db_table = "user_promo"
