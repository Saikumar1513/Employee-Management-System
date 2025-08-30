from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple root view
def home(request):
    return HttpResponse("Welcome to Employee Dashboard")

urlpatterns = [
    path('', home),                 # <-- root URL added
    path('admin/', admin.site.urls),
    path('api/', include('attendance.urls')),  # include other APIs as needed
]
