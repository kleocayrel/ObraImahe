from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email', 'age']
    USERNAME_FIELD = 'username'
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)


