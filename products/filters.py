from django_filters import rest_framework as filters

from products.models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        NUMERIC_FILTERS = ['lte', 'gte']
        model = Product
        fields = {
            'name': ['icontains'],
            'added_by': ['exact'],
            'kcal': NUMERIC_FILTERS,
            'protein': NUMERIC_FILTERS,
            'carb': NUMERIC_FILTERS,
            'fat': NUMERIC_FILTERS,
        }
