from django.dispatch import receiver
from django.db.models.signals import post_migrate
from .apps import UsersConfig
from .models.user import User


##################################################
# send signal when migrate has been finished
##################################################
@receiver(post_migrate, sender=UsersConfig)
def user_migrate(sender, **kwargs):
    '''
        This function will fire if any migration happens in the database
        will be check if the superuser already exists or not
        - if exists will continue the process
        - otherwise will create a new one
    '''
    if not User.objects.filter(username="root").exists():
        user = User.objects.create_superuser(first_name="admin", last_name="admin", username="root", type_account=1,
                                             email="admin@admin.com", phone="123")

        user.set_password("django123")
        user.save()
