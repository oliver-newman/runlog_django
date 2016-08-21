from django import forms
from .models import UserProfile, Shoe, Bike, Activity
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import date

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'date',
            'runToday', 'runMiles', 'runTime', 'shoe',
            'bikeToday', 'bikeMiles', 'bikeTime', 'bike',
            'title', 'comments', 'sleepHours',
        ]
        labels = {
            'runToday': _('Run'),
            'runMiles': _('Distance'),
            'runTime': _('Time'),
            'shoe': _('Shoe Used'),
            'bikeToday': _('Ride'),
            'bikeMiles': _('Distance'),
            'bikeTime': _('Time'),
            'bike': _('Bike Used'),
            'sleepHours': _('Hours of Sleep'),
        }
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'value': date.today()
            }),
            'comments': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = [
            'name', 'firstUseDate', 'mileage', 'notes', 'isDefault',
        ]
        labels = {
            'firstUseDate': _('First Used'),
            'isDefault': _('Default'),
        }
        widgets = {
            'firstUseDate': forms.DateInput(attrs={
                'type': 'date',
                'value': date.today()
            }),
            'notes': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = [
            'name', 'firstUseDate', 'mileage', 'notes', 'isDefault',
        ]
        labels = {
            'firstUseDate': _('First Used'),
            'isDefault': _('Default'),
        }
        widgets = {
            'firstUseDate': forms.DateInput(attrs={
                'type': 'date',
                'value': date.today()
            }),
            'notes': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }
        

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('isRunner', 'isCyclist')
        labels = {
            'isRunner': _('Runner'),
            'isCyclist': _('Cyclist'),
        }






