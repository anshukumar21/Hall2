from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from mess_site.models import ExtrasOrder
from django.core.mail import send_mail
from hall2temp.settings import EMAIL_HOST_USER
from .forms import MailForm
# Create your views here.

#View 1 : Shows Profile Page of the User upon login
@login_required
def profile_view(request):
    user = request.user
    return render(request,"profile.html",{'user':user})

@login_required
def user_dues_view(request):
    user = request.user
    user_dues = ExtrasOrder.objects.filter(username=user.username).values('order_month').annotate(total = Sum('item_map__extras_price')).order_by('-order_month')
    return render(request, 'dues_list.html', {'user_dues':user_dues})

@login_required
def mail_hec(request):
    user = request.user
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = str(data['subject'])
            body = str(data['body'])
            recepient_mail = 'sunrockers8@gmail.com'
            send_mail(subject,body,EMAIL_HOST_USER,[recepient_mail],fail_silently=False)
            return redirect('../mail_sent/')
    else:
        form = MailForm()
    return render(request,'send_mail.html',{'form':form})

def mail_sent(request):
    return render(request,'formsent.html')