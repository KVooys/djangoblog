from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post paths
    path("", views.post_list, name="post_list"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>", views.post_detail, name="post_detail"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("post/<int:pk>/comment/", views.post_comment, name="post_comment"),
    
    # user paths
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView, name="login"),
]
