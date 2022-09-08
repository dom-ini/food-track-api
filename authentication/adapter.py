from django.conf import settings
from django.contrib.auth.models import User
from allauth.account.utils import perform_login
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return f'{settings.FRONT_URL}/aktywuj-konto/{emailconfirmation.key}'


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        social_user = sociallogin.user
        if social_user.id:
            return
        try:
            user = User.objects.get(email=social_user.email)
            sociallogin.state['process'] = 'connect'
            perform_login(request, user, 'none')
        except User.DoesNotExist:
            pass
