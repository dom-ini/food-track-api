from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"

    def ready(self):
        import authentication.signals  # noqa: F401, pylint: disable=C0415,W0611
