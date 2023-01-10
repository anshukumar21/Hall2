from django.shortcuts import render, redirect
from .models import Announcement, Event
from .serializers import AnnouncementSerializer, EventSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .forms import AnnouncementForm, EventForm
# Create your views here.

@login_required
def make_announcement(request):
    user = request.user
    if user.is_staff:
        if request.method == "POST":
            username = user.username
            email = user.email
            form = AnnouncementForm(request.POST)
            if form.is_valid():
                data_dict = form.cleaned_data
                data_dict['username'] : username
                data_dict['email'] : email
                serializer = AnnouncementSerializer(data = data_dict)
                if serializer.is_valid():
                    serializer.save()
                    return redirect('home')
                else:
                    return Response("Error")
        return render(request,"send_announcement.html")
    else:
        return Response("Error")

@login_required
def add_event(request):
    user = request.user
    if user.is_staff:
        if request.method == "POST":
            username = user.username
            email = user.email
            form = EventForm(request.POST)
            if form.is_valid():
                data_dict = form.cleaned_data
                data_dict['username'] = username
                data_dict['email'] = email
                serializer = EventSerializer(data = data_dict)
                if serializer.is_valid():
                    serializer.save()
                    return redirect('home')
                else:
                    return Response("Error")
        return render(request,"send_event.html")
    else:
        return Response("Err0r")