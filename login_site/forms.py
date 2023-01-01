from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#This is a form which extends on the UserCreationForm class (asked in sign up page)
#contains extra fields email, first_name, last_name
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20,required=True)
    last_name = forms.CharField(max_length=20,required=True)

    class Meta:
        model = User 
        fields = ["email", "username", "first_name", "last_name", "is_staff", "password1", "password2"]