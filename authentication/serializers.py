from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, PasswordResetSerializer, UserDetailsSerializer
from rest_framework import serializers

from authentication.forms import CustomPasswordResetForm
from authentication.models import Profile


class CustomUserDetailsSerializer(UserDetailsSerializer):
    first_name = None
    last_name = None

    class Meta(UserDetailsSerializer.Meta):
        fields = ["id", "email"]


class CustomLoginSerializer(LoginSerializer):  # pylint: disable=W0223
    username = None


class CustomRegisterSerializer(RegisterSerializer):  # pylint: disable=W0223
    username = None


class CustomPasswordResetSerializer(PasswordResetSerializer):  # pylint: disable=W0223
    password_reset_form_class = CustomPasswordResetForm


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user"]
        read_only_fields = ["id", "user"]
