from rest_framework import pagination


class DiaryEntryPagination(pagination.PageNumberPagination):
    page_size = 100
