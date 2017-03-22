from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    house_keeper = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.housekeeper.email


class Room(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=64)

    def __str__(self):
        return self.room_name


class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=128)
    quantity = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    mode = models.NullBooleanField()
    value = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.device_name + self.functional
