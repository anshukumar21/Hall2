from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse
from .models import MessMain, MessExtras, ExtrasOrder
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessExtrasSerializer,MessMainSerializer, ExtrasOrderSerializer
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

#View 1 : This will output the list of items in regular menu
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

#View 2 : This will output the list of items in the extras menu
@api_view(['GET'])
def extras_menu_list(request):
    orders = MessExtras.objects.all().order_by('id')
    serializer = MessExtrasSerializer(orders, many=True)
    return Response(serializer.data) 