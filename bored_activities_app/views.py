
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .utils.mail_utils import *
from django.core.exceptions import ValidationError
from .models import Activity,Type,UserActivity
from .clients.bored_api import BoardedApi
from django.db import transaction
from .forms import EditForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from datetime import date
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            print(email)
            password = form.cleaned_data['password1']
            print(password)
            if not email_validation(email):
                return render(request, 'register.html', {'form': form, 'error_message': 'Invalid email format'})
            # if not password_validation(password):
            #     return render(request, 'register.html', {'form': form, 'error_message': 'Invalid password format'})
            with transaction.atomic():
                user = form.save()
                login(request, user)
                activity_type = request.POST.get('types')
                sync_relevant_activities(request=request,activity_type=activity_type)
                registered = send_verification_email()
                #if registered:
                return redirect('activity_list')
    else:
        form = UserCreationForm()
    types = Type.objects.all()
    return render(request, 'register.html', {'form': form,'types':types})

def sync_relevant_activities(request,activity_type):
    '''fetching activities and storing to database'''
    activities = BoardedApi.get_activities(activity_type)
    activity_list = []
    for activity_data in activities:
        activity = Activity(user=request.user, activity=activity_data['activity'])
        activity_list.append(activity)
    with transaction.atomic():
        try:
            Activity.objects.bulk_create(activity_list)
        except Exception as e:
            print(e)



def verify_email(request, key):
    key = request.META.get('KEY')
    if not key:
        raise ValidationError('Key is missing')



def activity_list(request):
    activities = Activity.objects.filter(user=request.user)
    paginator = Paginator(activities, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'activity_list.html', {'page_obj': page_obj})



@login_required
def update_activity(request, activity_id):
    print(activity_id)
    activity = Activity.objects.get(id=activity_id)
    if request.user != activity.user:
         raise ValidationError('Dont have the access to edit the activity')
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            activity.activity = data['activity']
            activity.save()
            return redirect('activity_list')
    else:
        form = EditForm()

    return render(request, 'edit_activity.html', {'activity': activity})



@login_required
@permission_required('activities.delete_activities', raise_exception=True)
def delete_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    raise PermissionDenied("You do not have permission to delete this activity.")


def fetch_activities(request):
    user_activity = UserActivity.objects.get(user=request.user)

    if user_activity.last_fetch_date != date.today():
        user_activity.activities_fetched_today = 0
        user_activity.last_fetch_date = date.today()
        user_activity.save()

    if request.method == 'POST' and user_activity.activities_fetched_today >= 2:
        return JsonResponse({'message': 'You can fetch a maximum of 2 activities per day.'})
    if request.method == 'POST':
        activity_type = request.POST.get('activity_type')
        response = BoardedApi.get_random_activity(activity_type)
        activity = response.json()
        Activity.objects.create(user=request.user, activity=activity['activity'])
        user_activity.activities_fetched_today += 1
        user_activity.save()
        return redirect('activity_list')
    types = Type.objects.all()
    return render(request, 'add_activity.html', {'types': types})




