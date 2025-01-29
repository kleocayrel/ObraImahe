from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, Artist, Comment,Category
from django.urls import reverse_lazy

class HomePage(TemplateView):
    template_name = 'App/home.html'

class AboutPage(TemplateView):
    template_name = 'App/about.html'

class FeedPage(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'App/Feed/feed.html'

class FeedDetail(DetailView):
    model = Post
    template_name = 'App/Feed/feed_detail.html'
    success_url = reverse_lazy('Feed')


class FeedCreate(CreateView):
    model = Post
    fields = ['text', 'image', 'title','artist','category', 'user']
    template_name = 'App/Feed/feed_create.html'
    success_url = reverse_lazy('Feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        context['categorys'] = Category.objects.all()
        context['users'] = User.objects.all()
        return context

class CommentCreate(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'App/Comment/comment_create.html'
    success_url = reverse_lazy('Feed_Detail')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Feed_Detail', kwargs={'pk': self.kwargs['pk']})


class FeedUpdate(UpdateView):
    model = Post
    fields = ['text', 'image', 'title', 'artist','category', 'user']
    template_name = 'App/Feed/feed_update.html'

class FeedDelete(DeleteView):
    model = Post
    template_name = 'App/Feed/feed_delete.html'
    success_url = reverse_lazy('Feed')

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['body','username']
    template_name = 'App/Comment/comment_update.html'
    def get_success_url(self):
        return reverse_lazy('Feed_Detail', kwargs={'pk': self.kwargs['pk']})


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'App/Comment/comment_delete.html'
    success_url = reverse_lazy('Feed')
