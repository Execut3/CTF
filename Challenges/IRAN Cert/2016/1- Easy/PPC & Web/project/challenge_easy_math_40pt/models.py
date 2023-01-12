from django.db import models
from django.contrib.auth.models import User


class SessionChallenge_easy_math(models.Model):
    user = models.OneToOneField(User)
    expiration_date = models.DateTimeField()
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    operator = models.CharField(max_length=10)
    result = models.IntegerField()