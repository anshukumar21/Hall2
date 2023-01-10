from django.urls import path
from . import views

#This App handles 5 URL's : for getting menu list, for adding menu items by manager, main menu page, extra's adding page, extras successfully added page

urlpatterns = [
    path('',views.mess_home,name='mess'),
    path('menu/',views.menu_view,name='menu'),
    path('manager/',views.manager_view,name='manager_view'),
    path('extraadded/',views.extra_added,name='extraadded'),
    path('orderextra/',views.order_extras,name='orderextra'),
]