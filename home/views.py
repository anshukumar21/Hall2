from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .serializers import QuerySerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def home_view(request):
    if request.method == "POST":
        data_dict = {
        "name" : request.POST["name"], 
        "email" : request.POST["email"], 
        "query" : request.POST["query"],}
        serializer = QuerySerializer(data = data_dict)
        if serializer.is_valid():
            serializer.save()
            return redirect('querysent')
        else:
            return Response("Error")
    else:
        return render(request,"index.html")

def gallery_view(request):
    return render(request,"gallery.html")

def query_sent_view(request):
    return render(request,"querysent.html")