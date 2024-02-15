from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("diary-entries", views.DiaryEntryViewSet, basename="diary_entries")
router.register("goals-entries", views.GoalsEntryViewSet, basename="goals_entries")

urlpatterns = [
    path("", include(router.urls)),
]
