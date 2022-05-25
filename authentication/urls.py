from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path, include, re_path

from authentication.views import FacebookLoginView, ProfileViewSet, GoogleLoginView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('facebook/', FacebookLoginView.as_view(), name='fb_login'),
    path('google/', GoogleLoginView.as_view(), name='google_login'),
    path('profiles/<int:pk>/', ProfileViewSet.as_view(), name='profiles'),

    path(
        'password/reset/confirm/<str:uidb64>/<str:token>/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
]
