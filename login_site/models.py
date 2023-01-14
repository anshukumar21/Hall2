from django.db import models
from django.contrib.auth.models import User

#Create Models Here

class User_OTP(models.Model):
    username = models.CharField(null=True,max_length=150)
    email = models.EmailField(null=True,max_length=50)
    otp_generated = models.IntegerField(null=True)