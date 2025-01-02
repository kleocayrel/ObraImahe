from django.db import models
from django.template.context_processors import media
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField (null=True, blank=True, upload_to='images/')
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "Feed/Detail",
            kwargs={
                "pk": self.pk
            })