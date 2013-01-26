from django.db import models
from django.utils import timezone


class Entry(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    description = models.TextField()
    reflection = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    occurred_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

