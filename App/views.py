from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, Author
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
    fields = ['text', 'image', 'title','user']
    template_name = 'App/feed_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['authors'] = Author.objects.all()
        return context


class FeedUpdate(UpdateView):
    model = Post
    fields = ['text', 'image', 'title', 'user']
    template_name = 'App/feed_update.html'

class FeedDelete(DeleteView):
    model = Post
    template_name = 'App/feed_delete.html'
    success_url = reverse_lazy('Feed')
