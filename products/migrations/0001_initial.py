# Generated by Django 4.0.3 on 2022-03-22 20:27

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
                (
                    "kcal_for_100",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0, message="kcal for 100 must be greater than 0")
                        ],
                    ),
                ),
                (
                    "protein_for_100",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="protein for 100 must be greater than 0"
                            )
                        ],
                    ),
                ),
                (
                    "carbo_for_100",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0, message="carbo for 100 must be greater than 0")
                        ],
                    ),
                ),
                (
                    "sugar_for_100",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0, message="sugar for 100 must be greater than 0")
                        ],
                    ),
                ),
                (
                    "fat_for_100",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0, message="fat for 100 must be greater than 0")
                        ],
                    ),
                ),
                (
                    "saturated_fat_for_100",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="saturated fat for 100 must be greater than 0"
                            )
                        ],
                    ),
                ),
                (
                    "portion_size",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0, message="portion size must be greater than 0")
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(editable=False)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "added_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="product", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
