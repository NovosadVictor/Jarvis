from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Home(models.Model):
    house_keeper = models.ForeignKey(User, on_delete=models.CASCADE)
    home_name = models.CharField(max_length=128, default='main house')
    address = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.house_keeper.username


class Room(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=64, default='my room')

    def __str__(self):
        return self.room_name


class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=128, default='my device')
    quantity = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    mode = models.NullBooleanField()
    value = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        index_together = [['id'],]

    def __str__(self):
        return self.device_name + self.description


class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image_url = models.URLField(default='/Jarvis/Desktop/Jarvis/Django/images')
    image_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return str(self.image_url)
