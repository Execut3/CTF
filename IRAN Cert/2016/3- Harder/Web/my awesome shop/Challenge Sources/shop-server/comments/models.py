from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    active = models.BooleanField(default=False)
    # status = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}, {1}'.format(self.user.username, self.comment[:20])
