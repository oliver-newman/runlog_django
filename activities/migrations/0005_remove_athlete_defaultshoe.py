# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20160816_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='defaultShoe',
        ),
    ]
