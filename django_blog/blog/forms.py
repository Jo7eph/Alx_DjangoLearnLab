from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django, python, backend)"
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill tags when editing
        if self.instance.pk:
            self.fields["tags"].initial = ", ".join(
                self.instance.tags.values_list("name", flat=True)
            )

    def save(self, commit=True, author=None):
        post = super().save(commit=False)
        if author is not None:
            post.author = author
        if commit:
            post.save()
            self._save_tags(post)
        return post

    def _save_tags(self, post):
        raw = self.cleaned_data.get("tags", "")
        names = [t.strip() for t in raw.split(",") if t.strip()]
        post.tags.clear()
        for name in names:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
