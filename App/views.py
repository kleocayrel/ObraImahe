from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, Artist, Comment, Category
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
    success_url = reverse_lazy('Feed')

class FeedCreate(CreateView):
    model = Post
    fields = ['text', 'image', 'title','artist','category', 'user']
    template_name = 'App/feed_create.html'
    success_url = reverse_lazy('Feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()
        return context

class CommentCreate(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'App/comment_create.html'
    success_url = reverse_lazy('Feed_Detail')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('Feed_Detail', kwargs={'pk': self.kwargs['pk']})


class FeedUpdate(UpdateView):
    model = Post
    fields = ['text', 'image', 'title', 'artist','category', 'user']
    template_name = 'App/feed_update.html'

class FeedDelete(DeleteView):
    model = Post
    template_name = 'App/feed_delete.html'
    success_url = reverse_lazy('Feed')


