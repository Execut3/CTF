from django.db import models
from django.contrib.auth.models import User


class SessionChallenge_prime_sum(models.Model):
    user = models.OneToOneField(User)
    expiration_date = models.DateTimeField()
    prime_number = models.IntegerField()