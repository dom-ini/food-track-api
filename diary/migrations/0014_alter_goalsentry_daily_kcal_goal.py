# Generated by Django 4.0.3 on 2022-05-17 17:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diary", "0013_alter_goalsentry_daily_carb_goal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goalsentry",
            name="daily_kcal_goal",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1, message="Wartość musi być większa od 0")]
            ),
        ),
    ]
