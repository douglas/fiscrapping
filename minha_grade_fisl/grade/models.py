from django.db import models


class Room(models.Model):
    capacity = models.IntegerField()
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    translation = models.BooleanField()


class Area(models.Model):
    description = models.TextField()
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)


class Author(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=200)
    candidate = models.IntegerField()


class Zone(models.Model):
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)


class Talk(models.Model):
    area = models.ForeignKey(Area)
    room = models.ForeignKey(Room)
    zone = models.ForeignKey(Zone)
    hour = models.CharField(max_length=2)
    title = models.CharField(max_length=200)
    date = models.DateField()
    abstract = models.TextField()
    level = models.CharField(max_length=150)
    authors = models.ManyToManyField('Author')
    minute = models.CharField(max_length=2)
