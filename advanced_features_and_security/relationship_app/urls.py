from django.urls import path
from LibraryProject.views import list_books, LibraryDetailView
# Mandatory imports for built-in auth views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Built-in views with specified template names
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # Custom registration view
    path('register/', views.register, name='register'),
]