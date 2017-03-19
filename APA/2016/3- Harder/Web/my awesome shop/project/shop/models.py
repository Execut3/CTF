from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, default='')
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(default='no flag here', max_length=80)

    def __unicode__(self):
        return self.name


class PurchasedItem(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.item.name


