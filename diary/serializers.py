from django.utils import timezone
from rest_framework import serializers

from diary.models import DiaryEntry, ProductEntry, GoalsEntry
from products.serializers import ProductSerializer


class ProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntry
        fields = ['id', 'product', 'weight']


class ProductEntryReadOnlySerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductEntry
        fields = ['id', 'product', 'weight']


class DiaryEntrySerializer(serializers.ModelSerializer):
    product_entry = ProductEntrySerializer(write_only=True)
    entry = ProductEntryReadOnlySerializer(read_only=True, source='product_entry')

    class Meta:
        model = DiaryEntry
        fields = ['id', 'product_entry', 'entry', 'meal', 'date']

    def create(self, validated_data):
        product_entry_data = validated_data.pop('product_entry', None)
        product_entry = ProductEntry.objects.create(**product_entry_data)
        diary_entry = DiaryEntry.objects.create(**validated_data, product_entry=product_entry)

        return diary_entry


class GoalsEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalsEntry
        fields = ['id', 'user', 'daily_kcal_goal', 'daily_protein_goal', 'daily_fat_goal', 'daily_carb_goal',
                  'from_date', 'created_at']
        read_only_fields = ['id', 'user', 'created_at', 'from_date']

