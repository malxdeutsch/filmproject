from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)


class Skill(models.Model):
    name = models.CharField(max_length=100)