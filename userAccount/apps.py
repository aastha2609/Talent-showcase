from django.apps import AppConfig


class UseraccountConfig(AppConfig):
    name = 'userAccount'

    def ready(self):
        import userAccount.signals
