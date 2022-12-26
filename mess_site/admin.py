from django.contrib import admin

# Register your models here.

#Admin has the ability to access MessMain and MessExtras db
from .models import MessMain,MessExtras
admin.site.register(MessMain)
admin.site.register(MessExtras)