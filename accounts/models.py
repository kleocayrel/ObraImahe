from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email', 'profile_pic']
    age = models.IntegerField(null=True)
    def __str__(self):
        return self.username