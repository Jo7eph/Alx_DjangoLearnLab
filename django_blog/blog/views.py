from django.shortcuts import render
from .models import Post

def home_view(request):
    return render(request, "blog/home.html")

def posts_view(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, "blog/posts.html", {"posts": posts})
