from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Post, Artist, Comment,Category
from django.urls import reverse_lazy
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


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
        context['categories'] = Category.objects.all()
        context['users'] = get_user_model().objects.all()
        return context

class FeedUpdate(UpdateView):
    model = Post
    fields = ['text', 'image', 'title', 'artist','category', 'user']
    template_name = 'App/Feed/feed_update.html'

class FeedDelete(DeleteView):
    model = Post
    template_name = 'App/Feed/feed_delete.html'
    success_url = reverse_lazy('Feed')

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']
    template_name = 'app/Comment/comment_create.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Feed_Detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'app/Comment/comment_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('Feed_Detail', kwargs={'pk': self.kwargs['post_pk']})

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'app/Comment/comment_delete.html'

    def get_object(self):
        return get_object_or_404(Comment, pk=self.kwargs['pk'], post__pk=self.kwargs['post_pk'])

    def get_success_url(self):
        return reverse_lazy('Feed_Detail', kwargs={'pk': self.kwargs['post_pk']})




def Feed_Detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent=None)  # Fetch top-level comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('Feed_Detail', pk=post.pk)

    return render(request, 'App/Feed/feed_detail.html', {
        'post': post,
        'comments': comments,
    })

def CommentReply(request, comment_id):
    parent_comment = get_object_or_404(Comment, id=comment_id)
    post = parent_comment.post
    if request.method == 'POST':
        form = CommentForm(request.POST)  # Removed parent_comment_id
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.parent = parent_comment  # Set parent comment
            new_comment.author = request.user
            new_comment.save()
            return redirect('Feed_Detail', pk=post.pk)

    return redirect('Feed_Detail', pk=post.pk)