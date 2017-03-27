#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class IP(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return str(self.ip_address)



