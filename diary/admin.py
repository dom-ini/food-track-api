from django.contrib import admin

from diary.models import DiaryEntry, ProductEntry, GoalsEntry

admin.site.register(DiaryEntry)
admin.site.register(ProductEntry)
admin.site.register(GoalsEntry)
