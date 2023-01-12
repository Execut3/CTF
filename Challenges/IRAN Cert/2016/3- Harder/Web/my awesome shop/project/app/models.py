from django.db import models
from django.contrib.auth.models import User


class Flag(models.Model):
    level = models.PositiveIntegerField(default=1)
    flag = models.CharField(max_length=100)


class ShopUser(models.Model):
    user = models.ForeignKey(User)
    budget = models.PositiveIntegerField(default=100)
    alias = models.CharField(max_length=9, default='shop user')
    identifier = models.CharField(max_length=32, default='')

    def __unicode__(self):
        return self.user.username
