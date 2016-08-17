from django.contrib import admin
from django.contrib.auth.models import User
from .models import Activity, Shoe, Bike

admin.site.register(Activity)
admin.site.register(Shoe)
admin.site.register(Bike)
