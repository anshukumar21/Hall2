from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import QueryResponse, Query
from .serializers import QueryResponseSerializer, QuerySerializer
from .forms import QueryForm
from rest_framework.response import Response
# Create your views here.

#View 1 : Shows Profile Page of the User upon login
@login_required
def profile_view(request):
    user = request.user
    return render(request,"profile.html",{'user':user})

def query_view(request):
    queries = Query.objects.all().order_by('-id')
    return render(request,'query_view.html',{'queries' : queries})

def send_query(request):
    if request.method == "POST":
        user = request.user
        form = QueryForm(request.POST)
        if form.is_valid():
            data_dict = form.cleaned_data
            data_dict['username'] = user.username
            data_dict['email'] = user.email
            serializer = QuerySerializer(data = data_dict)
            if serializer.is_valid():
                serializer.save()
                return redirect('../formsent/?name=query')
            else:
                return Response("Error")
    else:
        form = QueryForm()
    return render(request,"send_query.html",{'form':form})

def query_response(request):
    if request.method == "POST":
        user = request.user
        email = user.email
        username = user.username
        response = request.POST.get('response')
        id_map = request.POST.get('id_map')
        data_dict = {
            'email' : email,
            'username' : username,
            'response' : response,
            'id_map' : id_map,}
        serializer = QueryResponseSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            return redirect('../formsent/?name=response')
        else:
            return response("Error")
    else:
        id  = int(request.GET.get('id'))
        query_main = Query.objects.get(id = id)
        query_response = QueryResponse.objects.filter(id_map=id)
        return render(request, 'query_response.html', {'query_main':query_main,'query_response':query_response})

def form_sent_view(request):
    name = request.GET.get('name')
    form = {'name':name}
    return render(request,"query_resp_formsent.html",{'form':form})