from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee_count']
    
    def employee_count(self, obj):
        return obj.employees.count()
    employee_count.short_description = 'Employee Count'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'department', 'date_of_joining']
    list_filter = ['department', 'date_of_joining']
    search_fields = ['name', 'email']