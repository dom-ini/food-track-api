# Generated by Django 4.0.3 on 2022-05-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
