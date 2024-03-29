# Generated by Django 4.0.3 on 2022-03-28 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_barcode"),
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diaryentry",
            name="product",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="diary_entry",
                to="products.product",
            ),
        ),
    ]
