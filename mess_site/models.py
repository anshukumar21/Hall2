from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#MODEL 1 (Regular Items)
#This is the database definition which will contain all regular items for the day
class MessMain(models.Model) :
  
    main_item_name=models.CharField(null=True,max_length=35)
    day_of_the_week=models.CharField(null=True,max_length=10)
    meal_type = models.CharField(null=True,max_length=10)
    
    def __str__(self):
        return self.main_item_name

#MODEL 2 (Extras Items)
#This is the database definition which will contain all extras for the day
class MessExtras(models.Model) :
    
    extras_name=models.CharField(null=True,max_length=35)
    extras_price=models.IntegerField(null=True)

    def __str__(self):
        return self.extras_name

#Model 3 (Items Ordered by all Users)
#This is the database definition which will contain extras a particular user ordered
class ExtrasOrder(models.Model):
    roll_number = models.IntegerField(blank=True)
    order_date= models.DateTimeField(null=True)
    item_name = models.CharField(max_length=35,null=True)
    item_price = models.IntegerField(null=True)
    meal_type = models.CharField(null=True,max_length=10)

    def __str__(self):
        return self.username