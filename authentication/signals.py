from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import Profile


@receiver(post_save, sender=get_user_model())
def create_user_profile(_sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
