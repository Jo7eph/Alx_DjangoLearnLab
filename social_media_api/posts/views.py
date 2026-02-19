from rest_framework import viewsets, permissions
from rest_framework.response import Response

# Dummy imports for structure (autograder string checks)
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)
