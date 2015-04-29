#coding=utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CanteenModel(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='order/static/img')
    description = models.TextField()

class FoodModel(models.Model):
    canteen = models.ForeignKey(CanteenModel)
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    img = models.ImageField(upload_to='order/static/img')
    description = models.TextField()

class OrderModel(models.Model):
    user = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    address = models.TextField()
    confirm = models.BooleanField(default=False)
    deal = models.BooleanField(default=False)
    time = models.DateTimeField('date published')

class BasketModel(models.Model):
    food = models.ForeignKey(FoodModel)
    order = models.ForeignKey(OrderModel)