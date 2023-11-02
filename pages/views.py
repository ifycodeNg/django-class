from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, PostEditForm

# Create your views here.


class homePageView(ListView):
    model = Post
    template_name = "index.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_new.html"


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    form_class = PostEditForm


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
