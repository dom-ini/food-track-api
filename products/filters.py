from django_filters import rest_framework as filters

from products.models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        NUMERIC_FILTERS = ['lte', 'gte']
        model = Product
        fields = {
            'name': ['icontains'],
            'barcode': ['exact'],
            'added_by': ['exact'],
            'kcal_for_100': NUMERIC_FILTERS,
            'protein_for_100': NUMERIC_FILTERS,
            'carbo_for_100': NUMERIC_FILTERS,
            'sugar_for_100': NUMERIC_FILTERS,
            'fat_for_100': NUMERIC_FILTERS,
            'saturated_fat_for_100': NUMERIC_FILTERS,
        }
