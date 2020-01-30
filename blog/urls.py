from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView, CreateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, CommentCreateView, register
from .models import Post

urlpatterns = [
    # post paths
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail",),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/comment/", CommentCreateView.as_view(), name="post_comment"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),

    # user paths
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView, name="login"),
]
