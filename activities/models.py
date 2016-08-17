from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from uuid import uuid4

# Maximum distances allowed for runs and bike rides
MAX_RUN_DIST = 200
MAX_BIKE_DIST = 1000


class Shoe(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=64)
    firstUseDate = models.DateField(blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length = 256, blank=True, null=True)
    isDefault = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def addMileage(self, dist):
        self.mileage += dist

    # Overrides default save, setting isDefault to False on all other shoes
    # if set to True
    def save(self, *args, **kwargs):
        if self.isDefault:
            try:
                temp = Shoe.objects.get(isDefault=True)
                if self != temp:
                    temp.isDefault = False
                    temp.save()
            except Shoe.DoesNotExist:
                pass

        super(Shoe, self).save(*args, **kwargs)


class Bike(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=64)
    firstUseDate = models.DateField(blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length = 256, blank=True, null=True)
    isDefault = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def addMileage(self, dist):
        self.mileage += dist

    def save(self, *args, **kwargs):
        if self.isDefault:
            try:
                temp = Bike.objects.get(isDefault=True)
                if self != temp:
                    temp.isDefault = False
                    temp.save()
            except Bike.DoesNotExist:
                pass

        super(Bike, self).save(*args, **kwargs)


# Helper functions for Activity class
"""
Returns default shoe, for use in creating new activity
"""
def defaultShoe():
    return Shoe.objects.get(isDefault=True)
"""
# Returns default bike, for use in creating new activity
"""
def defaultBike():
    return Bike.objects.get(isDefault=True)


class Activity(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateField()

    runToday = models.BooleanField()
    runMiles = models.DecimalField(max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(MAX_RUN_DIST)],
        default=0)
    runTime = models.DurationField(blank=True, null=True)
    shoe = models.ForeignKey('activities.Shoe', blank=True, null=True,
            default=Shoe.objects.get(isDefault=True))

    bikeToday = models.BooleanField()
    bikeMiles = models.DecimalField(max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(MAX_BIKE_DIST)],
        default=0)
    bikeTime = models.DurationField(blank=True, null=True)
    bike = models.ForeignKey('activities.Bike', blank=True, null=True,
            default=defaultBike())

    title = models.CharField(max_length=64, blank=True, null=True)
    comments = models.CharField(max_length=2048, blank=True, null=True)
    sleepHours = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    class Meta:
        verbose_name_plural = "activities"

    def __init__(self, *args, **kwargs):
        super(Activity, self).__init__(*args, **kwargs)
        self.old_runMiles = self.runMiles
        self.old_bikeMiles = self.bikeMiles

    def __str__(self):
        activityString = str(self.date)

        if self.title:
            activityString += ": " + self.title

        return activityString

    # Override default save method, so that saving activity adjusts shoe miles
    def save(self, *args, **kwargs):
        if self.shoe:
            self.shoe.addMileage(self.runMiles - self.old_runMiles)
            self.shoe.save()
        if self.bike:
            self.bike.addMileage(self.bikeMiles - self.old_bikeMiles)
            self.bike.save()

        super(Activity, self).save(*args, **kwargs)
    






