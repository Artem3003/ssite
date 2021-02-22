from django.db import models

"""
Models and fields:
Singer:
    - title
    - Age
    - Albums [M2M]
    - Genre [M2M]
    - Tracks
Album:
    - title
    - Singer [FK]
    - Tracks [M2M]
Track:
    - title
    - Singer [FK]
    - Album [FK]
    - Genre [M2M]
    - duration
Genre:
    - title
"""

class Singer(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    age = models.PositiveSmallIntegerField(blank = True, null = True)

    def __str__(self):
        return f'{self.name}'

class Genre(models.Model):
    title = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return f'{self.title}'

class Album(models.Model):
    title = models.CharField(max_length=50, unique = True)
    author = models.ManyToManyField("Singer")
    tracks = models.ManyToManyField("Track")

    def __str__(self):
        return f'{self.title}'

class Track(models.Model):
    title = models.CharField(max_length=50, unique = True)
    author = models.ManyToManyField("Singer")
    duration = models.DurationField()
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return f'{self.title}'
