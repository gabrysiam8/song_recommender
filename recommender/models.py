from django.db import models


class Song(models.Model):
    artist = models.TextField()
    title = models.TextField()
    link = models.TextField()
    text = models.TextField()
