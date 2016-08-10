from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    runMileage = models.DecimalField(max_digits=10, decimal_places=2)
    bikeMileage = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.user.username
