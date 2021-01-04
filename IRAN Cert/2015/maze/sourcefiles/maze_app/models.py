from django.db import models

class Sessions(models.Model):
    username = models.CharField(max_length=20,unique=True)
    session_key = models.CharField(max_length=128, unique=True)
    expiration_date = models.DateTimeField()
    random_id = models.IntegerField(default=0)
    sequence_id = models.IntegerField(default=0)