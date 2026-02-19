from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("feed/", feed, name="feed"),
]

urlpatterns += router.urls
