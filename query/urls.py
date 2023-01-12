from django.urls import path
from . import views

#This App contains 4 URL : for showing list of all queries, for creating query, for sending comments, query/comment succesffuly sent 

urlpatterns = [
    path('queries/',views.query_view,name='queries'),
    path('queryresp/',views.query_response,name='queryresp'),
    path('formsent/',views.form_sent_view,name='formsent'),
    path('sendquery/',views.send_query,name='send_query'),
]