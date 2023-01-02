from django.urls import path
from . import views

#This App contains 1 URL : for showing profile page of user

urlpatterns = [
    path('queries/',views.query_view,name='queries'),
    path('queryresp/',views.query_response,name='queryresp'),
    path('formsent/',views.form_sent_view,name='formsent'),
    path('sendquery/',views.send_query,name='send_query'),
]