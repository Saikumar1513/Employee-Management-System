from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Count, Q
from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Department, Employee
from attendance.models import Attendance
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'date_of_joining']
    search_fields = ['name', 'email', 'phone_number']
    ordering_fields = ['name', 'date_of_joining']

@api_view(['GET'])
@permission_classes([AllowAny])
def department_stats(request):
    departments = Department.objects.annotate(
        employee_count=Count('employees')
    )
    
    data = {
        'labels': [dept.name for dept in departments],
        'data': [dept.employee_count for dept in departments]
    }
    
    return Response(data)

@api_view(['GET'])
@permission_classes([AllowAny])
def attendance_stats(request):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)
    
    attendance_data = Attendance.objects.filter(
        date__range=[start_date, end_date]
    ).values('date').annotate(
        present=Count('id', filter=Q(status='Present')),
        absent=Count('id', filter=Q(status='Absent')),
        late=Count('id', filter=Q(status='Late'))
    ).order_by('date')
    
    dates = []
    present_data = []
    absent_data = []
    late_data = []
    
    for entry in attendance_data:
        dates.append(entry['date'].strftime('%Y-%m-%d'))
        present_data.append(entry['present'])
        absent_data.append(entry['absent'])
        late_data.append(entry['late'])
    
    data = {
        'dates': dates,
        'present': present_data,
        'absent': absent_data,
        'late': late_data
    }
    
    return Response(data)

def charts_view(request):
    return render(request, 'charts.html')