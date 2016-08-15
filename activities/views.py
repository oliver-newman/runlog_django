from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Activity, Shoe, Bike
from .forms import ActivityForm, ShoeForm, BikeForm

from django.http import HttpResponse # TODO: just for testing - remove this


def index(request):
    context_dict = {}

    return render(request, 'activities/activities.html', context_dict)


#-------------------------------------------------------------------------------
# Activity views

def activity_list(request):
    activities = Activity.objects.order_by('date').reverse()
    context_dict = {
        'activities': activities
    }

    return render(request, 'activities/activity_list.html', context_dict)


"""
Info about existing activity with primary key pk
"""
def activity_detail(request, pk):
    act = get_object_or_404(Activity, pk=pk)

    context_dict = {
        'act': act
    }

    return render(request, 'activities/activity_detail.html', context_dict)


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


def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)

        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/edit_activity.html', context_dict)


#-------------------------------------------------------------------------------
# Shoe views

def shoe_list(request):
    return HttpResponse("Shoe list")


def shoe_detail(request, pk):
    return HttpResponse("Shoe detail")


def new_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
    else:
        form = ShoeForm()

    context_dict = {
        'form': ShoeForm(),
    }

    return render(request, 'activities/edit_shoe.html', context_dict)


def edit_shoe(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)


    if request.method == "POST":
        form = ShoeForm(request.POST, instance=shoe)

        if form.is_valid():
            shoe = form.save()
            return redirect('shoe_detail', pk=shoe.pk)
    else:
        form = ShoeForm(instance=shoe)

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/edit_shoe.html', context_dict)

    
#-------------------------------------------------------------------------------
# Bike views

def bike_list(request):
    return HttpResponse("Bike list")


def bike_detail(request, pk):
    return HttpResponse("Bike detail")


def new_bike(request):
    if request.method == "POST":
        form = BikeForm(request.POST)
    else:
        form = BikeForm()

    context_dict = {
        'form': BikeForm(),
    }

    return render(request, 'activities/edit_bike.html', context_dict)


def edit_bike(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    if request.method == "POST":
        form = ShoeForm(request.POST, instance=shoe)

        if form.is_valid():
            shoe = form.save()
            return redirect('shoe_detail', pk=shoe.pk)
    else:
        form = ShoeForm(instance=shoe)

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/edit_shoe.html', context_dict)






