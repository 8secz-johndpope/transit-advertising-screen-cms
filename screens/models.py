from datetime import timedelta
from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    class Meta(object):
        ordering = ['name']

    def __str__(self):
        return self.name


class Screen(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    priority = models.PositiveSmallIntegerField(default=0)
    seconds = models.PositiveSmallIntegerField(default=60)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=now)
    due_date = models.DateTimeField(default=now)

    class Meta(object):
        ordering = ['priority', '-modified_at', '-created_at']

    def __str__(self):
        return self.text
