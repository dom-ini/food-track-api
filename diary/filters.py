from django_filters import rest_framework as filters

from diary.models import DiaryEntry


class DiaryEntryFilter(filters.FilterSet):
    class Meta:
        model = DiaryEntry
        fields = {
            "date": ["exact"],
            "meal": ["exact"],
        }
