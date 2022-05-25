from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer, PasswordResetSerializer
from rest_framework import serializers

from authentication.forms import CustomPasswordResetForm
from authentication.models import Profile


class CustomUserDetailsSerializer(UserDetailsSerializer):
    first_name = None
    last_name = None

    class Meta(UserDetailsSerializer.Meta):
        fields = ['id', 'email']


class CustomLoginSerializer(LoginSerializer):
    username = None


class CustomRegisterSerializer(RegisterSerializer):
    username = None


class CustomPasswordResetSerializer(PasswordResetSerializer):
    password_reset_form_class = CustomPasswordResetForm


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user']
        read_only_fields = ['id', 'user']
