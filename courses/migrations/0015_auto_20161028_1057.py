# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_course_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=160),
        ),
    ]