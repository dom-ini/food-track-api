from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "is_verified"]
    actions = ["make_verified"]

    @admin.action(description="Zweryfikuj wybrane produkty")
    def make_verified(self, _request, queryset):
        queryset.update(is_verified=True)


admin.site.register(Product, ProductAdmin)
