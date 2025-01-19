from django.db import models
from django.template.context_processors import media
from django.urls import reverse


class Artist(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)
    image = models.ImageField (null=True, blank=True, upload_to='images/')
    artist = models.ManyToManyField("Artist", related_name="artists")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "Feed_Detail",
            kwargs={
                "pk": self.pk
            })

class Comment(models.Model):
    post = models.ForeignKey("Post",related_name="comments", on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s - %s' % (self.post.title, self.username)
