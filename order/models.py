#coding=utf-8

from django.db import models

# Create your models here.

class Canteen(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='order/static/img')
    description = models.TextField()

class FoodModel(models.Model):
    canteen = models.ForeignKey(Canteen)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='order/static/img')
    description = models.TextField()