from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import Profile


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):  # pylint: disable=W0613
    if created:
        Profile.objects.create(user=instance)
