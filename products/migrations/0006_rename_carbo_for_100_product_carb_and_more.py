# Generated by Django 4.0.3 on 2022-08-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_is_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='carbo_for_100',
            new_name='carb',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='fat_for_100',
            new_name='fat',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='kcal_for_100',
            new_name='kcal',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='protein_for_100',
            new_name='protein',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='saturated_fat_for_100',
            new_name='saturated_fat',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sugar_for_100',
            new_name='sugar',
        ),
    ]