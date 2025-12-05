from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('student.urls')),   # or the app name you created
    path('admin/', admin.site.urls),
]
