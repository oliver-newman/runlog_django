from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Shoe, Bike, Activity

admin.site.register(UserProfile)
admin.site.register(Shoe)
admin.site.register(Bike)
admin.site.register(Activity)
