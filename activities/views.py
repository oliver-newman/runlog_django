from django.shortcuts import render
from .models import Activity, Shoe, Bike

USERNAME = "orn688"

def index(request):
    context_dict = {}

    return render(request, 'activities/activities.html', context_dict)


def activity_list(request):
    # activities = Activity.objects.filter(user=USERNAME).order_by('date')
    activities = Activity.objects.order_by('date')
    context_dict = {'activities': activities}

    return render(request, 'activities/activity_list.html', context_dict)
    

