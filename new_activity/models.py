from __future__ import unicode_literals

from django.db import models

class Activity(models.Model):
    activityId = models.PositiveIntegerField(unique=True)
    user = models.ForeignKey('auth.User')
    date = models.DateField()
    ranToday = models.BooleanField()
    runMiles = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    runTime = models.DurationField(blank=True, null=True)
    shoe = models.ForeignKey('new_activity.Shoe', blank=True, null=True)
    bikedToday = models.BooleanField()
    bikeMiles = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bikeTime = models.DurationField(blank=True, null=True)
    bike = models.ForeignKey('new_activity.Bike', blank=True, null=True)
    sleepHours = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    title = models.CharField(max_length=64, blank=True, null=True)
    comments = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        verbose_name_plural = "activities"

    def __str__(self):
        selfString = str(self.date)
        if not self.title.isspace():
            selfString.append(": {title}".format(title=self.title))

        return selfString


class Shoe(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=64)
    firstUseDate = models.DateField(blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length = 256, blank=True, null=True)
    isDefault = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def addMileage(dist):
        self.mileage += dist

    def setDefault():
        isDefault = True

    def setNotDefault():
        isDefault = False


class Bike(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=64)
    firstUseDate = models.DateField(blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length = 256, blank=True, null=True)
    isDefault = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def addMileage(dist):
        self.mileage += dist

    def setDefault():
        isDefault = True

    def setNotDefault():
        isDefault = False



