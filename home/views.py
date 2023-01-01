from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def home_view(request):
    return render(request,"index.html")

def gallery_view(request):
    return render(request,"gallery.html")