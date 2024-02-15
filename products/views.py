from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    ordering_fields = [
        "name",
        "kcal",
        "protein",
        "carb",
        "fat",
    ]
    ordering = ["name"]

    def get_queryset(self):
        added_by = self.request.query_params.get("added_by")
        if not added_by:
            return Product.objects.filter(is_verified=True)
        return self.get_products_added_by_current_user()

    def get_products_added_by_current_user(self):
        user = self.request.user
        if user.is_authenticated:
            return Product.objects.filter(added_by=user, is_verified=True)
        return Product.objects.none()

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsAdminUser]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
