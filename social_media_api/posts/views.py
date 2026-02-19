from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Post, Like

# If your project notifications app exists here:
try:
    from notifications.models import Notification
except Exception:
    Notification = None

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created and Notification is not None:
            Notification.objects.create(recipient=post.author, actor=request.user, verb="liked your post", target=post)

        return Response({"detail": "liked"})


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"detail": "unliked"})
