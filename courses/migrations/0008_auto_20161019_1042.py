# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20161019_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='courses',
            new_name='course',
        ),
    ]
