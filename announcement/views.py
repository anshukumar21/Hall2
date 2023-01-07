from django.shortcuts import render, redirect
from .models import Announcement
from .serializers import AnnouncementSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
# Create your views here.

@login_required
def make_announcement(request):
    user = request.user
    if user.is_staff:
        if request.method == "POST":
            username = user.username
            email = user.email
            announcement = request.POST.get('announcement')
            data_dict = {
                'username' : username,
                'email' : email,
                'announcement' : announcement,
            }
            serializer = AnnouncementSerializer(data = data_dict)
            if serializer.is_valid():
                serializer.save()
                return redirect('home')
            else:
                return Response("Error")
        return render(request,"send_announcement.html")
    else:
        return Response("Error")