from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profiles(models.Model):
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    avatar = models.CharField(max_length=100, default='avatar1.png')

