#coding=utf-8
__author__ = 'esoragoto'

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User

import json
import models
from MobileFoodOrderServer import settings

def register(request):
    if request.method == 'GET':
        return HttpResponse("error")
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        email = data['email']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            response_data = {
                'response': 'succeed'
            }
        else:
            response_data = {
                'response': 'error'
            }
        return HttpResponse(json.dumps(response_data), content_type='text/json')

def login(request):
    if request.method == 'GET':
        return HttpResponse("Get")
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response_data = {
                'response': 'succeed',
                'username': request.user.username
            }
        else:
            response_data = {
                'response': 'error',
                'username': request.user.username
            }
        return HttpResponse(json.dumps(response_data), content_type='text/json')

def changepw(request):
    if request.method == 'GET':
        return HttpResponse()

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        response_data = {
            'response': 'succeed'
        }
        return HttpResponse(json.dumps(response_data), content_type='text/json')

def userinfo(request):
    print request
    if request.method == 'GET':
        print request.user
        response_data = {
            'response': 'succeed',
            'user': [
                request.user.username,
                request.user.email,
                str(request.user.is_superuser),
                str(request.user.last_login)
                ]
        }
        return HttpResponse(json.dumps(response_data), content_type='text/json')

def food(request):
    if request.method == 'GET':
        choose = int(request.GET['choose'])
        response_data = {
            'response': 'succeed',
            'STATIC_URL': settings.STATIC_URL,
            'food': []
        }
        if choose == 0:
            food_list = list(models.FoodModel.objects.all())
            for p in food_list:
                # print p.name, p.img, p.canteen.name, p.description
                food_data = {
                    'name': p.name,
                    'img': str(p.img),
                    'canteen': p.canteen.name,
                    'description': p.description
                }
                food_data = json.dumps(food_data)
                food_data = food_data.encode('utf8')
                food_data = food_data.encode('utf8')
                food_data = json.loads(food_data)
                # food_data = str(food_data)
                # print type(response_data['food']), response_data['food']
                print type(food_data), food_data
                response_data['food'].append(food_data)
                # print response_data['food']
            response_data = json.dumps(response_data)
            # response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
            # print response_data
        # return HttpResponse(response_data, content_type='text/json')
    return HttpResponse('error')