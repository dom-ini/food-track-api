from django.contrib import admin

from products.models import Product


@admin.action(description="Zweryfikuj wybrane produkty")
def make_verified(_modeladmin, _request, queryset):
    queryset.update(is_verified=True)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "is_verified"]
    actions = [make_verified]


admin.site.register(Product, ProductAdmin)
