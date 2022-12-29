from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse
from .models import MessMain, MessExtras, ExtrasOrder
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessExtrasSerializer,MessMainSerializer, ExtrasOrderSerializer
import datetime
from django.contrib.auth.decorators import login_required
from urllib.error import HTTPError
from urllib.parse import urlparse

# Create your views here.

#View 1: This function redirects user based on staff status (if not logged in redirects to login page)
@api_view(['GET'])
def mess_home(request):
    if(request.user.is_staff==True):
        return redirect('manager_view')
    elif request.user.is_staff==False:
        return redirect('menu')

#View 2 : This will output the list of items in regular menu (Redundant as of now)
@api_view(['GET'])
def main_menu_list(request):
    #breakfast menu will be on display from 7am-10am
    #lunch menu will be on display from 12pm-3pm
    #dinner menu will be on display from 7pm-10pm
    current_time = datetime.datetime.now()
    breakfast_start = current_time.replace(hour=6,minute=0, second=0, microsecond=0)
    breakfast_end =  current_time.replace(hour=10,minute=0, second=0, microsecond=0)
    lunch_start =  current_time.replace(hour=11,minute=0, second=0, microsecond=0)
    lunch_end =  current_time.replace(hour=15,minute=0, second=0, microsecond=0)
    dinner_start =  current_time.replace(hour=18,minute=0, second=0, microsecond=0)
    dinner_end =  current_time.replace(hour=22,minute=0, second=0, microsecond=0)
    if breakfast_start <= current_time <= breakfast_end:
        orders =  MessMain.objects.filter(meal_type='breakfast').order_by('id').values()
        serializer = MessMainSerializer(orders, many=True)
        return Response(serializer.data)
    elif lunch_start <= current_time <= lunch_end:
        orders =  MessMain.objects.filter(meal_type='lunch').order_by('id').values()
        serializer = MessMainSerializer(orders, many=True)
        return Response(serializer.data)
    elif dinner_start <= current_time <= dinner_end:
        orders =  MessMain.objects.filter(meal_type='dinner').order_by('id').values()
        serializer = MessMainSerializer(orders, many=True)
        return Response(serializer.data)
    else:
        return Response('Menu Unavailable')

#View 3 : This will output the list of items in the extras menu (Redundant as of now)
@api_view(['GET'])
def extras_menu_list(request):
    orders = MessExtras.objects.all().order_by('id')
    serializer = MessExtrasSerializer(orders, many=True)
    return Response(serializer.data)

#View 4 : This will output the list of all items in the menu (Doesnt display all items...only provision to display one item each)
@login_required
def menu_view(request):
    i=1
    context={}
    for object in MessExtras.objects.all():
        context["Extras_"+str(i)] = object.extras_name
        context["price_"+str(i)] = object.extras_price
        i=i+1

    i=1
    for object in MessMain.objects.all():
        context["Main_"+str(i)] = object.main_item_name
        context["Day_"+str(i)] = object.day_of_the_week
        i=i+1
    return render(request,'mess.html', context)


#View 5 : Can only be seen by the manager and 
@api_view(['GET','POST'])
def manager_view(request):
    if request.user.is_staff == True:
        if request.method == "POST":
            post_data = request.data
            if int(post_data["main"]) == 0:
                data_dict = {"extras_name" : post_data["extras_name"], "extras_price" : post_data["extras_price"]}
                serializer = MessExtrasSerializer(data = data_dict)
            else:
                data_dict = {
                "main_item_name" : post_data["main_item_name"],
                "day_of_the_week" : post_data["day_of_the_week"], 
                "type_of_meal" : post_data["type_of_meal"],}
                serializer = MessMainSerializer(data = data_dict)
            if serializer.is_valid():
                serializer.save()
                return redirect('/mess_site/manager/')
        return render(request,'manager.html')
    else:
        return render(request,"404error.html")