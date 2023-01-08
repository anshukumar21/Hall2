from django.contrib import admin

# Register your models here.
from .models import Announcement, Event
admin.site.register(Announcement)
admin.site.register(Event)