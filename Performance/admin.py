from django.contrib import admin
from .models import Performance

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'rating', 'review_date']
    list_filter = ['rating', 'review_date', 'employee__department']
    search_fields = ['employee__name']
    date_hierarchy = 'review_date'