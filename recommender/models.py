from django.db import models
from django.contrib.postgres.fields import ArrayField


class Mood(models.Model):
    name = models.TextField()
    categories = ArrayField(models.TextField())
