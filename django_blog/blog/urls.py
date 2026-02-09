from django.urls import path
from .views import (
    PostListView,  # already
    PostsByTagListView,
    SearchResultsView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),

    path("tags/<slug:tag_slug>/", PostsByTagListView.as_view(), name="posts_by_tag"),
    path("search/", SearchResultsView.as_view(), name="search"),
]
