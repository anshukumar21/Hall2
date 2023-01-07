from django.db import models
import datetime
# Create your models here.
class Announcement(models.Model) :
  
    username = models.CharField(null=True,max_length=150)
    email=models.CharField(null=True,max_length=50)
    announcement = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.username + ' ' + str(self.date)