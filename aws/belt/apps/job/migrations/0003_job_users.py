# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-20 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20190920_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='users',
            field=models.ManyToManyField(related_name='users_jobs', to='job.User'),
        ),
    ]