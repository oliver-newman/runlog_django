# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_remove_athlete_defaultshoe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='user',
        ),
        migrations.DeleteModel(
            name='Athlete',
        ),
    ]