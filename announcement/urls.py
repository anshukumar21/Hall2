from django.urls import path
from . import views

urlpatterns = [
    path('makeannouncement/',views.make_announcement,name='make_announcement'),
]