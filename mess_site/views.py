from django.shortcuts import render, redirect
from .models import MessMain, MessExtras, ExtrasOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessExtrasSerializer,MessMainSerializer, ExtrasOrderSerializer
import datetime
from django.contrib.auth.decorators import login_required
from .forms import OrderForm

# Create your views here.

@login_required
def mess_home(request):
    user = request.user
    return render(request,'mess_home.html',{'user':user})

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
        return orders
    elif lunch_start <= current_time <= lunch_end:
        orders =  MessMain.objects.filter(meal_type='lunch').order_by('id').values()
        return orders
    elif dinner_start <= current_time <= dinner_end:
        orders =  MessMain.objects.filter(meal_type='dinner').order_by('id').values()
        return orders
    else:
        return None

#View 3 : This will output the list of items in the extras menu (Redundant as of now)
@api_view(['GET'])
def extras_menu_list(request):
    orders = MessExtras.objects.all().order_by('id')
    serializer = MessExtrasSerializer(orders, many=True)
    return Response(serializer.data)

def menu_view(request):
    extras = MessExtras.objects.all()
    mains =  MessMain.objects.all()
    return render(request,'mess_menu.html', {'mains':mains,'extras':extras})

#View 4 : This will output the list of all items in the menu (Doesnt display all items...only provision to display one item each)
@login_required
def order_extras(request):
    user = request.user
    if not user.is_staff:
        extras = MessExtras.objects.all()
        if request.method == "POST":
            username = user.username
            email = user.email
            ordered_ids = request.POST.getlist('order')
            extras_items = []
            for id in ordered_ids:
                extras_items.append(MessExtras.objects.get(id = int(id)))
            order_date = datetime.date.today()
            extra_order = ExtrasOrder.objects.create(username = username, email = email, order_date = order_date)
            for item in extras_items:
                extra_order.item_id.add(item)
            return redirect('extraadded')
        extras = MessExtras.objects.all()
        return render(request,'extras_order.html', {'extras':extras})
    else:
        return render(request,"404error.html")

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
                return redirect('/mess_site/')
        return render(request,'manager.html')
    else:
        return render(request,"404error.html")

@login_required
def extra_added(request):
    user = request.user
    if not user.is_staff:
        orders = ExtrasOrder.objects.all()
        return render(request,"add_extra_success.html",{'orders':orders})
    else:
        return render(request,"404error.html")