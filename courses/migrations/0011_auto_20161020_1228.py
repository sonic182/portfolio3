# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20161019_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='place',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
    ]
