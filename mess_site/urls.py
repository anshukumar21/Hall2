from django.urls import path
from . import views

#This App handles 2 URL's : for getting main menu list, for getting extras menu list

urlpatterns = [
    path('main_menu_list/',views.main_menu_list,name='main_menu_list'),
    path('extras_menu_list/',views.extras_menu_list,name='extras_menu_list'),
]