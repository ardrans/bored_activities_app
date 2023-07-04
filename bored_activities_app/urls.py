from django.urls import path
from . import views


urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('register/', views.register, name='register'),
    path('verify_email/<str:key>/', views.verify_email, name='verify_email'),
    path('update_activity/<int:activity_id>/', views.update_activity, name='edit_activity'),
    path('delete_activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('fetch_activities/', views.fetch_activities, name='fetch_activities'),
]