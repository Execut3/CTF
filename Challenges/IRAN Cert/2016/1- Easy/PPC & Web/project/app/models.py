from django.db import models
from django.contrib.auth.models import User


class Flag(models.Model):
    challenge = models.CharField(max_length=20)
    flag = models.CharField(max_length=100)