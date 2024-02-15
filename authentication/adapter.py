from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.contrib.auth.models import User


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return f"{settings.FRONT_URL}/aktywuj-konto/{emailconfirmation.key}"


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        social_user = sociallogin.user
        if social_user.id or not social_user.email:
            return
        try:
            user = User.objects.get(email=social_user.email)
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass
