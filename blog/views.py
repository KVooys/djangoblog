from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.


def post_list(request):
    # order by reversed date, so newest post is on top
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by(
        "-created_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=post).order_by(
        "-created_date"
    )
    return render(request, "blog/post_detail.html", {"post": post, "comments": comments})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
        return render(request, "blog/post_edit.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, "blog/post_edit.html", {"form": form})


def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Add post_id as foreign key
            form.instance.post_id=pk
            comment = form.save()
            return redirect("post_detail", pk=pk)
    else:
        form = CommentForm()
        return render(request, "blog/post_comment.html", {"form": form, "post": post})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, "blog/registration/register.html", {"form": form})
