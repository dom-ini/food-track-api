# Generated by Django 4.0.3 on 2022-04-02 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_remove_diaryentry_dish_entry_and_more'),
        ('products', '0003_dish'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dish',
        ),
    ]