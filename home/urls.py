from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('gallery/',views.gallery_view,name='gallery'),
    path('querysent/',views.query_sent_view,name='querysent'),
]