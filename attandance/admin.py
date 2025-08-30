from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'date', 'status')  # match model fields
    list_filter = ('date', 'status')                     # remove non-existent field
    search_fields = ('employee_name',)                  # optional

admin.site.register(Attendance, AttendanceAdmin)
