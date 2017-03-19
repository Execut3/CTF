from django.db import models


class flag(models.Model):
    name = models.CharField(max_length=100)
