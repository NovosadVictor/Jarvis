# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='home_name',
            field=models.CharField(default='main house', max_length=128),
            preserve_default=False,
        ),
    ]
