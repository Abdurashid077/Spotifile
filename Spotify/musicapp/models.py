from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    yonaliw = models.CharField(max_length=15, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)


class Album(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    cover = models.URLField(blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)



class Song(models.Model):
    title = models.CharField(max_length=30)
    cover = models.URLField(blank=True)
    lyrics = models.TextField(blank=True)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    source = models.URLField()









