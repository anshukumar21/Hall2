from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from .forms import SignUpForm, OTPForm, ForgotPasswordForm
from django.contrib.auth import logout, update_session_auth_hash, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import math, random, secrets, string
from .models import User_OTP
from django.core.mail import send_mail, BadHeaderError
from hall2temp.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def generateOTP():
     digits = "0123456789"
     otp = ""
     for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
     return otp

def generatePassword():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd = ''
    for i in range(10):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd

#View 0 : For handling error
def handler404(request, *args, **argv):
    return render(request,'404error.html')

#View 1 : To Sign Up a User according to the in built User model and the form defined in .forms
def sign_up_view(request):
    if request.method == "POST" :
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            otp = generateOTP()
            user_otp = User_OTP(username=user.username,email = user.email ,otp_generated=otp)
            user_otp.save()
            subject = 'Activate Your Account'
            message = 'Your OTP for verification is : ' + str(otp)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently=False)
            return redirect('otp_verify',username = user.username)
        else:
            return HttpResponse("Form Invalid")
    else:
        form = SignUpForm()
    return render(request,"login.html",{'form':form})

def otp_verify(request, username):
    if request.method=='POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            otp_given = int(data['otp'])
            otp_required = User_OTP.objects.get(username = username).otp_generated
            if otp_given == otp_required:
                user = User.objects.get(username=username)
                user.is_active = True
                user.save()
                user_otp = User_OTP.objects.get(username=username)
                user_otp.delete()
                return redirect('login')
            else:
                return HttpResponse("OTP Wrong")
        else:
            return HttpResponse("Form Invalid")
    else:
        form = OTPForm()
    return render(request,'otp_enter.html',{'form':form})

#View 2 : To Login a User who has already signed up. Upon succesful login it redirects to Profile page
def login_view(request):
    if request.method == "POST" :
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/userprofile/profile/')
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})

#View 3 : To log out a user who has already logged in
@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

#View 4 : To change password of the user. Available in the login/signup page (!Doesnt make sense needs change)
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = ForgotPasswordForm(request.POST)
        if password_reset_form.is_valid():
            username = password_reset_form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                subject = "Password Reset Requested"
                email_template_name = "password_reset_email.txt"
                c = {
				"email":user.email,
				'domain':'127.0.0.1:8000',
				'site_name': 'Website',
				"uid": urlsafe_base64_encode(force_bytes(user.pk)),
				"user": user,
				'token': default_token_generator.make_token(user),
				'protocol': 'http',
				}
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, EMAIL_HOST_USER , [user.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect ("password_reset_done")
            except:
                return HttpResponse('User doesnt exist')
    password_reset_form = ForgotPasswordForm()
    return render(request=request, template_name="password_reset_form.html", context={"password_reset_form":password_reset_form})