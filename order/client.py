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
    print request.POST
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
        response_data = json.dumps(response_data)
        print response_data
        return HttpResponse(response_data, content_type='text/json')

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
    print "request.POST", request.POST
    if request.method == 'GET':
        print "GET request.user", request.user
        response_data = {
            'response': 'succeed',
            'user': [
                request.user.username,
                request.user.email,
                str(request.user.is_superuser),
                str(request.user.last_login)
                ]
        }
    elif request.POST:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)
        response_data = {
            'response': 'succeed',
            'user': [
                user.username,
                user.email,
                str(user.is_superuser),
                str(user.last_login)
                ]
        }
    response_data = json.dumps(response_data)
    return HttpResponse(response_data, content_type='text/json')

def food(request):
    print request.user
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
                food_data = {
                    'id': p.id,
                    'name': p.name,
                    'img': str(p.img),
                    'canteen': p.canteen.name,
                    'description': p.description
                }
                response_data['food'].append(food_data)
            response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
            # print "after encoding", type(response_data), response_data
        else:
            food_list = list(models.FoodModel.objects.filter(id=choose))
            for p in food_list:
                food_data = {
                    'id': p.id,
                    'name': p.name,
                    'img': str(p.img),
                    'canteen': p.canteen.name,
                    'description': p.description
                }
                response_data['food'].append(food_data)
            response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
            # print "after encoding", type(response_data), response_data

        return HttpResponse(response_data, content_type='text/json')
    return HttpResponse('error')