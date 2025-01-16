from django.db import models
from django.template.context_processors import media
from django.urls import reverse


class Author(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField (null=True, blank=True, upload_to='images/')
    user = models.ManyToManyField(Author,related_name='users')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "Feed/Detail",
            kwargs={
                "pk": self.pk
            })

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.text

class Tag(models.Model):
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField("Post", related_name="tags")