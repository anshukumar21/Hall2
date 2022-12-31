from django.db import models

# Create your models here.
class Query(models.Model) :
  
    name = models.CharField(null=True,max_length=50)
    email=models.CharField(null=True,max_length=30)
    query = models.TextField(null=True)
    date_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + ' ' + str(self.date_time)