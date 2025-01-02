from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomePage(TemplateView):
    template_name = 'App/home.html'

class AboutPage(TemplateView):
    template_name = 'App/about.html'

class FeedPage(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'App/feed.html'

class FeedDetail(DetailView):
    model = Post
    template_name = 'App/feed_detail.html'

class FeedCreate(CreateView):
    model = Post
    fields = ['author', 'text', 'image', 'title']
    template_name = 'App/feed_create.html'

class FeedUpdate(UpdateView):
    model = Post
    fields = ['author', 'text', 'image', 'title']
    template_name = 'App/feed_update.html'

class FeedDelete(DeleteView):
    model = Post
    template_name = 'App/feed_delete.html'
    success_url = reverse_lazy('Feed')