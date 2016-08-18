# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20160816_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]