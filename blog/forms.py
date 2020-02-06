from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = ("title", "text")


class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=100)
    text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ("author", "text")
