from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("posts/", views.posts_view, name="posts"),
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="posts_by_tag"),
]
