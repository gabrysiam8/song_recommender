from django.db import models
from django.contrib.postgres.fields import ArrayField


class Song(models.Model):
    artist = models.TextField()
    title = models.TextField()
    link = models.TextField()
    text = models.TextField()


class Mood(models.Model):
    name = models.TextField()
    categories = ArrayField(models.TextField())
