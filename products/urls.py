from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
