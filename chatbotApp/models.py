from django.db import models

# Create your models here.
#created database for products

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=400,blank=True)
    availability_status = models.BooleanField(default=True)
    tag = models.CharField(max_length=100)