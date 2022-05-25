from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return f'{settings.FRONT_URL}/aktywuj-konto/{emailconfirmation.key}'
