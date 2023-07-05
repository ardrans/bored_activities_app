
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .utils.mail_utils import *
from django.core.exceptions import ValidationError
from .models import Activity,Type,UserActions,UserProfile
from .clients.bored_api import BoardedApi
from django.db import transaction
from .forms import EditForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from .utils.redis_utils import RedisUtil
from datetime import date

redis_client = RedisUtil()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if not email_validation(email):
                return render(request, 'register.html', {'form': form, 'error_message': 'Invalid email format'})
            with transaction.atomic():
                user = form.save()
                login(request, user)
                activity_type = request.POST.get('types')
                sync_relevant_activities(request=request,activity_type=activity_type)
                status = send_verification_email()
                if status:
                    return redirect('get_activities')
    else:
        form = UserCreationForm()
    activity_types = Type.objects.all()
    return render(request, 'register.html', {'form': form,'types':activity_types})

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
    secret_token = request.GET.get('KEY')
    if not secret_token:
        raise ValidationError('secret token is missing')
    user_mail = redis_client.get(secret_token)
    if not user_mail:
        raise ValidationError('invalid key')
    user = UserProfile.objects.get(email=user_mail)
    user.email_verified = True
    user.save()
    return HttpResponse('Email verification successful!')



def get_activities(request):
    activities = Activity.objects.filter(user=request.user)
    paginator = Paginator(activities, 3)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'activity_list.html', {'page_obj': page_obj})

def edit_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == 'POST':
        activity.edit_mode = not activity.edit_mode
        activity.save()
        return redirect('get_activities')
    return render(request, 'activity_list.html', {'page_obj': Activity.objects.all()})
@login_required
def update_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.user != activity.user:
        raise ValidationError('You do not have access to edit this activity.')
    form = EditForm(request.POST)
    if form.is_valid():
        activity.activity = form.cleaned_data['activity']
        activity.edit_mode = False
        activity.save()
    return redirect('get_activities')

@login_required
@permission_required('activities.delete_activities', raise_exception=True)
def delete_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == 'DELETE':
        activity.delete()
        return redirect('get_activities')
    raise PermissionDenied("You do not have permission to delete this activity.")


def insert_activity(request):
    today = date.today()
    #user_action, created = UserActions.objects.get_or_create(user=request.user)

    user_activity_created_count = UserActions.objects.filter(
        user=request.user,
        activity_type='activities_fetched',
        created_at__date=today
    ).count()

    if user_activity_created_count > 2:
        print(user_activity_created_count)
        return {'message': 'You have already fetched 2 activities today. Try again tomorrow.'}
    if request.method == 'POST':
        activity_type = request.POST.get('activity_type')
        activity = BoardedApi.get_random_activity(activity_type)
        Activity.objects.create(user=request.user, activity=activity['activity'])
        UserActions.objects.create(user=request.user,activity_type = 'activities_fetched')
        #UserActions.save()
        return redirect('get_activities')
    types = Type.objects.all()
    return render(request, 'add_activity.html', {'types': types})




