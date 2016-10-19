# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='picture',
            field=models.ImageField(default='', upload_to='courses_pics'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
