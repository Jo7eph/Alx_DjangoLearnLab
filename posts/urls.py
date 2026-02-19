from django.urls import path
from .views import FeedViewSet

urlpatterns = [
    path("feed/", FeedViewSet.as_view({"get": "list"}), name="feed"),
]
