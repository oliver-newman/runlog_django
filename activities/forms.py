from django import forms
from .models import Activity, Shoe, Bike

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('date',
                  'runToday', 'runMiles', 'runTime', 'shoe',
                  'bikeToday', 'bikeMiles', 'bikeTime', 'bike',
                  'title', 'comments', 'sleepHours',)


class ShoeForm(forms.ModelForm):

    class Meta:
        model = Shoe
        fields = ('name', 'firstUseDate', 'mileage', 'notes',
                  'isDefault',)


class BikeForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = ('name', 'firstUseDate', 'mileage', 'notes',
                'isDefault',)
        
