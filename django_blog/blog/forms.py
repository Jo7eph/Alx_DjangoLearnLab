from django import forms
from taggit.forms import TagWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),
            "title": forms.TextInput(attrs={"placeholder": "Post title"}),
            "content": forms.Textarea(attrs={"rows": 6, "placeholder": "Write your post..."}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment..."}),
        }
