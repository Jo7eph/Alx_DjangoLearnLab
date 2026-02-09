from django.shortcuts import render
from .models import Post
from django.db.models import Q

def home_view(request):
    return render(request, "blog/home.html")

def posts_view(request):
    query = request.GET.get("q")

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()

    return render(request, "blog/posts.html", {
        "posts": posts,
        "query": query
    })
