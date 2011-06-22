from django.db import models

class Room(models.Model):
    capacity = models.IntegerField()
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)


class Area(models.Model):
    description = models.TextField()
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

class Author(models.Model):
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

class Zone(models.Model):
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

class Talk(models.Model):
    area = models.ForeignKey(Area)
    room = models.ForeignKey(Room)
    zone = models.ForeignKey(Zone)
    hour = models.TimeField()
    minute = models.TimeField()
    date = models.DateField()
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    level = models.CharField(max_length=150)
