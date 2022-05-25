from rest_framework import viewsets, pagination

from diary.filters import DiaryEntryFilter
from diary.models import DiaryEntry, GoalsEntry
from diary.pagination import DiaryEntryPagination
from diary.serializers import DiaryEntrySerializer, GoalsEntrySerializer


class DiaryEntryViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryEntrySerializer
    filterset_class = DiaryEntryFilter
    ordering_fields = ['meal', 'date']
    ordering = ['created_at']
    pagination_class = DiaryEntryPagination

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        queryset = DiaryEntry.objects.filter(user=current_user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GoalsEntryViewSet(viewsets.ModelViewSet):
    serializer_class = GoalsEntrySerializer
    ordering = ['-created_at']

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        queryset = GoalsEntry.objects.filter(user=current_user.id)
        return queryset

    def filter_queryset(self, queryset):
        from_date = self.request.query_params.get('from_date')
        if from_date:
            queryset = queryset.filter(from_date__lte=from_date).order_by('-from_date', '-created_at')
            if queryset.exists():
                goal = queryset.first()
                queryset = queryset.filter(id=goal.id)
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
