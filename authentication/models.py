from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(
        'auth.User',
        related_name='profile',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Profile: {self.id}, user: {self.user.email}'
