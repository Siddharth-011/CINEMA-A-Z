from django.db import models

# Create your models here.
class Liked(models.Model):
    user = models.CharField(max_length=16)
    movie = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'liked'


class Titles(models.Model):
    name = models.CharField(max_length=150)
    year = models.TextField()  # This field type is a guess.
    imdb = models.CharField(unique=True, max_length=150)
    mc = models.CharField(max_length=150, blank=True, null=True)
    rt = models.CharField(max_length=150, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    cast = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'


class Towatch(models.Model):
    user = models.CharField(max_length=16)
    movie = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'towatch'


class Watched(models.Model):
    user = models.CharField(max_length=16)
    movie = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'watched'
