#coding=utf-8
__author__ = 'esoragoto'

from django import forms

class CanteenForm(forms.Form):
    name = forms.CharField(label='名称')
    img = forms.ImageField(label='图片')
    description = forms.CharField(label='描述',widget=forms.Textarea)

class FoodForm(forms.Form):
    name = forms.CharField(label='名称')
    img = forms.ImageField(label='图片')
    price = forms.FloatField(label='单价')
    canteen = forms.IntegerField(label="食堂")
    description = forms.CharField(label='描述',widget=forms.Textarea)