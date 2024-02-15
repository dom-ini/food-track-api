# Generated by Django 4.0.3 on 2022-05-17 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diary", "0012_alter_goalsentry_from_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goalsentry",
            name="daily_carb_goal",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
                    django.core.validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="goalsentry",
            name="daily_fat_goal",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
                    django.core.validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="goalsentry",
            name="daily_kcal_goal",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
                    django.core.validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="goalsentry",
            name="daily_protein_goal",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
                    django.core.validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="productentry",
            name="weight",
            field=models.DecimalField(
                decimal_places=1,
                default=0,
                max_digits=6,
                validators=[django.core.validators.MinValueValidator(1, message="Waga musi być większa od 0")],
            ),
        ),
    ]
