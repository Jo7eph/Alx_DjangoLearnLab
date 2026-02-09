from django.shortcuts import render
from .models import Post
from django.db.models import Q
from django.views.generic import ListView
from taggit.models import Tag

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
class PostByTagListView(ListView):
    model = Post
    template_name = "blog/posts_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        tag = Tag.objects.get(slug=tag_slug)
        return Post.objects.filter(tags__in=[tag]).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = Tag.objects.get(slug=self.kwargs.get("tag_slug"))
        return context
