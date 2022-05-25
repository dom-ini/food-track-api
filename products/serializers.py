from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'barcode', 'kcal_for_100', 'protein_for_100', 'carbo_for_100', 'sugar_for_100',
                  'fat_for_100', 'saturated_fat_for_100', 'portion_size']
