# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_activity', '0004_auto_20160809_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='bike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_activity.Bike'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='bikeMiles',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='activity',
            name='runMiles',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='activity',
            name='shoe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_activity.Shoe'),
        ),
    ]
