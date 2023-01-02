from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#View 1 : Shows Profile Page of the User upon login
@login_required
def profile_view(request):
    user = request.user
    return render(request,"profile.html",{'user':user})