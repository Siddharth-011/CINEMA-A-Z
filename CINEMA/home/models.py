from django.db import models

# Create your models here.

class Titles(models.Model):
    name = models.CharField(max_length=150)
    year = models.TextField()  # This field type is a guess.
    imdb = models.CharField(unique=True, max_length=150)
    mc = models.CharField(max_length=150, blank=True, null=True)
    rt = models.CharField(max_length=150, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    cast = models.CharField(max_length=100, blank=True, null=True)
    id = models.IntegerField(blank=False, null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'titles'

class Towatch(models.Model):
    user = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    movie = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'towatch'


class Watched(models.Model):
    user = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    movie = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'watched'

class Liked(models.Model):
    user = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    movie = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'liked'


class Cache(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.CharField(max_length=300, blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)
    runtime = models.CharField(max_length=20, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    plot = models.CharField(max_length=500, blank=True, null=True)
    rimdb = models.CharField(max_length=10, blank=True, null=True)
    r1mc = models.CharField(max_length=10, blank=True, null=True)
    r2mc = models.CharField(max_length=10, blank=True, null=True)
    mc1r = models.CharField(max_length=10, blank=True, null=True)
    mc1 = models.TextField(blank=True, null=True)
    mc2r = models.CharField(max_length=10, blank=True, null=True)
    mc2 = models.TextField(blank=True, null=True)
    imdb1r = models.CharField(max_length=10, blank=True, null=True)
    imdb1h = models.CharField(max_length=100, blank=True, null=True)
    imdb1 = models.TextField(blank=True, null=True)
    imdb2r = models.CharField(max_length=10, blank=True, null=True)
    imdb2h = models.CharField(max_length=100, blank=True, null=True)
    imdb2 = models.TextField(blank=True, null=True)
    seasoninfo = models.CharField(max_length=200, blank=True, null=True)
    rt1 = models.TextField(blank=True, null=True)
    rt2 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=15, blank=True, null=True)
    r1rt = models.CharField(max_length=10, blank=True, null=True)
    r2rt = models.CharField(max_length=10, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    cast = models.CharField(max_length=150, blank=True, null=True)
    sim1 = models.IntegerField(blank=True, null=True)
    sim1h = models.CharField(max_length=300, blank=True, null=True)
    sim2 = models.IntegerField(blank=True, null=True)
    sim2h = models.CharField(max_length=300, blank=True, null=True)
    sim3 = models.IntegerField(blank=True, null=True)
    sim3h = models.CharField(max_length=300, blank=True, null=True)
    sim4 = models.IntegerField(blank=True, null=True)
    sim4h = models.CharField(max_length=300, blank=True, null=True)
    v = models.CharField(max_length=300, blank=True, null=True)
    p = models.CharField(max_length=300, blank=True, null=True)
    amc = models.CharField(max_length=300, blank=True, null=True)
    nf = models.CharField(max_length=300, blank=True, null=True)
    h = models.CharField(max_length=300, blank=True, null=True)
    ap = models.CharField(max_length=300, blank=True, null=True)
    dp = models.CharField(max_length=300, blank=True, null=True)
    hm = models.CharField(max_length=300, blank=True, null=True)
    pp = models.CharField(max_length=300, blank=True, null=True)
    atp = models.CharField(max_length=300, blank=True, null=True)
    s = models.CharField(max_length=300, blank=True, null=True)
    a = models.CharField(max_length=300, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cache'