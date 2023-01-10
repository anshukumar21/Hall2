from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from announcement.models import Announcement, Event
# Create your views here.

#View 1 : Homepage where announcements, events will be displayed (The dynamic part)
def home_view(request):
    announcements = Announcement.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-event_date')
    return render(request,"index.html",{'announcements':announcements,'events':events})
