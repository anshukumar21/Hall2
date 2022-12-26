from django.urls import path
from . import views

#This App contains 1 URL : for showing profile page of user

urlpatterns = [
    path('profile/',views.profile_view ,name='profile'),
]