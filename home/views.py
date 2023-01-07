from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from announcement.models import Announcement
# Create your views here.

@api_view(['GET','POST'])
def home_view(request):
    announcements = Announcement.objects.all()
    return render(request,"index.html",{'announcements':announcements})

def gallery_view(request):
    return render(request,"gallery.html")