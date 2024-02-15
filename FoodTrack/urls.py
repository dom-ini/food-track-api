from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from diary.urls import router as diary_router
from products.urls import router as products_router

router = routers.DefaultRouter()
router.registry.extend(products_router.registry)
router.registry.extend(diary_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/auth/", include("authentication.urls")),
]

schema_url = path(
    "api/v1/openapi/",
    get_schema_view(title="FoodTrack", description="API for FoodTrack - online food diary"),
    name="openapi-schema",
)
docs_url = path(
    "api/v1/docs/",
    TemplateView.as_view(template_name="docs.html", extra_context={"schema_url": "openapi-schema"}),
    name="swagger-ui",
)

if settings.DEBUG:
    urlpatterns += [schema_url, docs_url]
