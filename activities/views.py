from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from .models import Activity, Shoe, Bike
from .forms import ActivityForm, ShoeForm, BikeForm, UserForm, UserProfileForm

from django.http import HttpResponse # TODO: just for testing - remove this

RUN_FIELDS = ['runMiles', 'runTime', 'shoe']
BIKE_FIELDS = ['bikeMiles', 'bikeTime', 'bike']

def home(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username=username, password=password)

    # if user is not None:
        # login(request, user)
        # return redirect('activity_list')

    context_dict = {}
    return render(request, 'activities/home.html', context_dict)


#-------------------------------------------------------------------------------
# Login/user views

def user_login(request):
    """
    User login view
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # If user with matching credentials was found
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/activities/')
            else:
                # Inactive account
                return HttpResonseRedirect('/activities/failed_login/')
        else:
            print "Invalid login details for username {0}".format(username)
            # TODO: Say this in a reload of user_login view
            return HttpResponse("Invalid login details entered.")
    else:
        context_dict = {}

        return render(request, 'activities/login.html', context_dict)


def failed_login(request):
    # TODO: create a view and template for this
    return HttpResponse("Your account is disabled.")


def register(request):
    """
    User registration view
    """
    register = False

    if request.method == 'POST':
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()

            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print userForm.errors, profileForm.errors

    else:
        userForm = UserForm()
        profileForm = UserProfileForm()

    context_dict = {
        'userForm': userForm,
        'profileForm': profileForm
    }

    return render(request, 'activities/register.html', context_dict)


#-------------------------------------------------------------------------------
# Activity views

def activity_list(request):
    activities = Activity.objects.filter(user=request.user).order_by('date').reverse()
    context_dict = {
        'activities': activities
    }

    return render(request, 'activities/activity_list.html', context_dict)


def activity_detail(request, pk):
    """
    Info about existing activity with primary key pk
    """
    act = get_object_or_404(Activity, pk=pk)

    context_dict = {
        'act': act
    }

    return render(request, 'activities/activity_detail.html', context_dict)


def activity_new(request):
    if request.method == 'POST':
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
        'runFields': RUN_FIELDS,
        'bikeFields': BIKE_FIELDS
    }

    return render(request, 'activities/activity_edit.html', context_dict)


def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)

        if request.POST.get('delete'):
            activity.delete()
            return redirect('activity_list')

        elif form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)

    context_dict = {
        'form': form,
        'runFields': RUN_FIELDS,
        'bikeFields': BIKE_FIELDS
    }

    return render(request, 'activities/activity_edit.html', context_dict)


#-------------------------------------------------------------------------------
# Shoe views

def shoe_list(request):
    shoes = Shoe.objects.filter(user=request.user).order_by('isDefault').reverse()
    context_dict = {
        'shoes': shoes
    }

    return render(request, 'activities/shoe_list.html', context_dict)


def shoe_detail(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)

    context_dict = {
        'shoe': shoe
    }

    return render(request, 'activities/shoe_detail.html', context_dict)


def shoe_new(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST)

        if form.is_valid():
            shoe = form.save(commit=False)
            shoe.user = request.user
            shoe.save()

            return redirect('shoe_detail', pk=shoe.pk)

    else:
        form = ShoeForm()

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/shoe_edit.html', context_dict)


def shoe_edit(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)

    if request.method == 'POST':
        form = ShoeForm(request.POST, instance=shoe)

        if form.is_valid():
            shoe = form.save()
            return redirect('shoe_detail', pk=shoe.pk)
    else:
        form = ShoeForm(instance=shoe)

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/shoe_edit.html', context_dict)

    
#-------------------------------------------------------------------------------
# Bike views

def bike_list(request):
    bikes = Bike.objects.filter(user=request.user).order_by('isDefault').reverse()
    context_dict = {
        'bikes': bikes
    }

    return render(request, 'activities/bike_list.html', context_dict)


def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    context_dict = {
        'bike': bike
    }

    return render(request, 'activities/bike_detail.html', context_dict)


def bike_new(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)

        if form.is_valid():
            bike = form.save(commit=False)
            bike.user = request.user
            bike.save()

            return redirect('bike_detail', pk=bike.pk)

    else:
        form = BikeForm()

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/bike_edit.html', context_dict)


def bike_edit(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)

        if form.is_valid():
            bike = form.save()
            return redirect('bike_detail', pk=bike.pk)
    else:
        form = BikeForm(instance=bike)

    context_dict = {
        'form': form,
    }

    return render(request, 'activities/bike_edit.html', context_dict)


#-------------------------------------------------------------------------------
# About page

def about(request):
    context_dict = {}

    return render(request, "activities/about.html", context_dict)




