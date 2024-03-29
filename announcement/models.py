from django.db import models
import datetime
# Create your models here.

#Model 1 : Database features for the Anouncements Made by Admin Users
class Announcement(models.Model) :
  
    username = models.CharField(null=True,max_length=150)
    email=models.CharField(null=True,max_length=50)
    announcement = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.username + ' ' + str(self.date)

#Model 2 : Database fields for the Events added by Admin Users
class Event(models.Model):
    username = models.CharField(null=True,max_length=150)
    email = models.CharField(null=True,max_length=50) 
    event_date = models.DateField(null=True)
    event_time = models.TimeField(default=datetime.time.min)
    event_headline = models.CharField(null=True,max_length=150)

    def __str__(self):
        return self.event_headline + ' ' + str(self.event_date)
