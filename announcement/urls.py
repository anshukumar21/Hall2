from django.urls import path
from . import views

#This App handles 2 URL's : for posting announcement, for posting event

urlpatterns = [
    path('makeannouncement/',views.make_announcement,name='make_announcement'),
    path('addevent',views.add_event,name='add_event'),
]