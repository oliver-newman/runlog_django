# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_activity', '0002_auto_20160809_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='bikeTime',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='comments',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='runTime',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='firstUseDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='firstUseDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]