from django.db import models
from django.contrib.auth.models import User


class SessionChallenge_simple_post(models.Model):
    user = models.OneToOneField(User)
    expiration_date = models.DateTimeField()
    random_number = models.IntegerField()