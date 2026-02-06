from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # Import this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # Endpoint to get a token:
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]