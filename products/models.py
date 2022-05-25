from django.core import validators
from django.db import models
from django.utils import timezone


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    added_by = models.ForeignKey(
        'auth.User',
        related_name='product',
        null=False,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=128,
        null=False,
    )
    barcode = models.CharField(
        max_length=13,
        null=True,
        blank=True,
    )
    kcal_for_100 = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='kcal for 100 must be greater than 0'),
        ],
    )
    protein_for_100 = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='protein for 100 must be greater than 0'),
        ],
    )
    carbo_for_100 = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='carbo for 100 must be greater than 0'),
        ],
    )
    sugar_for_100 = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='sugar for 100 must be greater than 0'),
        ],
    )
    fat_for_100 = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='fat for 100 must be greater than 0'),
        ],
    )
    saturated_fat_for_100 = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='saturated fat for 100 must be greater than 0'),
        ],
    )
    portion_size = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(0, message='portion size must be greater than 0'),
        ],
    )
    is_verified = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        editable=False
    )
    is_deleted = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - kcal {self.kcal_for_100}/B {self.protein_for_100}' \
               f'/WW {self.carbo_for_100}/T {self.fat_for_100}'
