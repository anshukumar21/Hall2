from django.urls import path
from . import views

#This App contains 1 URL : for showing profile page of user

urlpatterns = [
    path('profile/',views.profile_view ,name='profile'),
    path('dues/',views.user_dues_view,name='user_dues'),
    path('mailhec/',views.mail_hec,name='mail_hec'),
    path('mail_sent/',views.mail_sent,name='mail_sent'),
]