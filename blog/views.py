from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.

class PostListView(generic.ListView):
    """
    Post list, reverse sorted by date
    """
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    queryset = Post.objects.order_by("-created_date")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    """
    A post and its comments, reverse sorted by date
    """
    model = Post
    template_name = "blog/post_detail.html"
    
    def get_context_data(self, **kwargs):
        # Get context
        context = super(PostDetailView, self).get_context_data(**kwargs)
        
        # Get the post id from the "pk" URL parameter and add it to the context
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk']).order_by("-created_date")
        return context

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name ="blog/post_edit.html"
    fields = ["title", "text"]

    def form_valid(self, form):
        # Add user as author to post
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self): 
        return reverse("post_list")


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "text"]

    def get_success_url(self): 
        return reverse("post_detail", kwargs={'pk': self.kwargs['pk']})


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name ="blog/post_comment.html"
    fields = ["author", "text"]
    
    def get_context_data(self, **kwargs):
        # Get context
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        
        # Get the post id from the "pk" URL parameter and add it to the context
        context['post'] = Post.objects.filter(id=self.kwargs['pk']).get()
        return context

    def get_success_url(self): 
        return reverse("post_detail", kwargs={'pk': self.kwargs['pk']})


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
