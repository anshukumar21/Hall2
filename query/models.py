from django.db import models
import datetime
# Create your models here.

class Query(models.Model) :
  
    username = models.CharField(null=True,max_length=150)
    email=models.CharField(null=True,max_length=50)
    query = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.name + ' ' + str(self.id) + ' ' + str(self.date)

class QueryResponse(models.Model):
    email = models.EmailField(blank=False)
    username = models.CharField(blank=False,max_length=150)
    response = models.TextField(blank=False)
    id_map = models.IntegerField(blank=False,default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.username + ' ' + str(self.date)