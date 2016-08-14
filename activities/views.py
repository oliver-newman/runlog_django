from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity, Shoe, Bike
from .forms import ActivityForm, ShoeForm, BikeForm

USERNAME = "orn688"

def index(request):
    context_dict = {}

    return render(request, 'activities/activities.html', context_dict)


def activity_list(request):
    activities = Activity.objects.order_by('date').reverse()
    context_dict = {
        'activities': activities
    }

    return render(request, 'activities/activity_list.html', context_dict)


def new_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()

            return redirect('activity_detail', pk=activity.pk)

    else:
        form = ActivityForm()

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/edit_activity.html', context_dict)


def activity_detail(request, pk):
    act = get_object_or_404(Activity, pk=pk)

    context_dict = {
        'act': act
    }

    return render(request, 'activities/activity_detail.html', context_dict)


def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)

        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            """
            activity.date = request.date
            activity.runToday = request.runToday
            activity.runMiles = request.runMiles
            activity.runTime = request.runTime
            activity.shoe = request.shoe
            activity.bikeToday = request.bikeToday
            activity.bikeMiles = request.bikeMiles
            activity.bikeTime = request.bikeTime
            activity.bike = request.bike
            activity.title = request.title
            activity.comments = request.comments
            activity.sleepHours = request.sleepHours
            activity.save()
            """

            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/edit_activity.html', context_dict)


def new_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
    else:
        form = ShoeForm()

    context_dict = {
        'form': ShoeForm(),
    }

    return render(request, 'activities/edit_shoe.html', context_dict)
    

def new_bike(request):
    if request.method == "POST":
        form = BikeForm(request.POST)
    else:
        form = BikeForm()

    context_dict = {
        'form': BikeForm(),
    }

    return render(request, 'activities/edit_bike.html', context_dict)
