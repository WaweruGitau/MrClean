# clean/models.py
from django.db import models


# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)

class Order(models.Model):
    client = models.CharField(max_length=50, default= 'Unknown')
    item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    delivery_date = models.DateField()
