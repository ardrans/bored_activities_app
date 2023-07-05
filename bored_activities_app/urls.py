from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_activities, name='get_activities'),
    path('register/', views.register, name='register'),
    path('verify_email/<str:key>/', views.verify_email, name='verify_email'),
    path('update_activity/<int:activity_id>/', views.update_activity, name='update_activity'),
    path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('delete_activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('insert_activity/', views.insert_activity, name='insert_activity'),
]