# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-26 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0004_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='home_name',
            field=models.CharField(default='my favorite house', max_length=128),
        ),
        migrations.AlterIndexTogether(
            name='device',
            index_together=set([('id',)]),
        ),
    ]
