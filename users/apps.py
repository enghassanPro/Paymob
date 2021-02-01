from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import user_migrate

        post_migrate.connect(user_migrate, sender=self)
