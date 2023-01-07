from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from announcement.models import Announcement, Event
# Create your views here.

@api_view(['GET','POST'])
def home_view(request):
    announcements = Announcement.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-event_date')
    return render(request,"index.html",{'announcements':announcements,'events':events})

def gallery_view(request):
    return render(request,"gallery.html")