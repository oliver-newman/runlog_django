from __future__ import unicode_literals

from django.db import models

class Activity(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateField()
    runToday = models.BooleanField()
    runMiles = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    runTime = models.DurationField(blank=True, null=True)
    shoe = models.ForeignKey('new_activity.Shoe', blank=True, null=True)
    bikeToday = models.BooleanField()
    bikeMiles = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bikeTime = models.DurationField(blank=True, null=True)
    bike = models.ForeignKey('new_activity.Bike', blank=True, null=True)
    sleepHours = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    title = models.CharField(max_length=64, blank=True, null=True)
    comments = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        verbose_name_plural = "activities"

    def __str__(self):
        activityString = str(self.date)

        if self.hasTitle():
            activityString += ": " + self.title

        return activityString

    # Return whether or not title field is empty
    def hasTitle(self):
        return not (self.title == "" or self.title.isspace())
    

class Shoe(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey('auth.User')
    firstUseDate = models.DateField(blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length = 256, blank=True, null=True)
    isDefault = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def addMileage(dist):
        self.mileage += dist

    def setAsDefault():
        self.isDefault = True

    def setAsNotDefault():
        self.isDefault = False


class Bike(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey('auth.User')
    firstUseDate = models.DateField(blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length = 256, blank=True, null=True)
    isDefault = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def addMileage(dist):
        self.mileage += dist

    def setAsDefault():
        self.isDefault = True

    def setAsNotDefault():
        self.isDefault = False




