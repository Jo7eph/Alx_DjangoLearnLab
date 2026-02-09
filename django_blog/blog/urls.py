from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home_view, register_view, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)


urlpatterns = [
    path("", home_view, name="home"),

    # Required by checker (singular)
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Keep these for browsing (and your navbar)
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Auth
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
