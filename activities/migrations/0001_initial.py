# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 15:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('runToday', models.BooleanField()),
                ('runMiles', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('runTime', models.DurationField(blank=True, null=True)),
                ('bikeToday', models.BooleanField()),
                ('bikeMiles', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bikeTime', models.DurationField(blank=True, null=True)),
                ('sleepHours', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('comments', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('firstUseDate', models.DateField(blank=True, null=True)),
                ('mileage', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('notes', models.CharField(blank=True, max_length=256, null=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('firstUseDate', models.DateField(blank=True, null=True)),
                ('mileage', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('notes', models.CharField(blank=True, max_length=256, null=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='bike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.Bike'),
        ),
        migrations.AddField(
            model_name='activity',
            name='shoe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.Shoe'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
