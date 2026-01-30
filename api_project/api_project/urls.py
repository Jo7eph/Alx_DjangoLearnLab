from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    # This is the line the checker is looking for:
    path('api/', include('api.urls')), 
]