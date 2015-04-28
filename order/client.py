#coding=utf-8
__author__ = 'esoragoto'

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
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
    return HttpResponse("unknown error")

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
            if user.is_superuser:
                response_data = {
                    'response': 'error',
                    'username': request.user.username
                }
            else:
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

def change_pw(request):
    if request.method == 'GET':
        return HttpResponse()

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        response_data = {
            'response': 'succeed'
        }
        return HttpResponse(json.dumps(response_data), content_type='text/json')

def user_info(request):
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
                    'price': str(p.price),
                    'img': str(p.img),
                    'canteen': p.canteen.name,
                    'description': p.description
                }
                response_data['food'].append(food_data)
            response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
        else:
            food_list = list(models.FoodModel.objects.filter(id=choose))
            for p in food_list:
                food_data = {
                    'id': p.id,
                    'name': p.name,
                    'price': str(p.price),
                    'img': str(p.img),
                    'canteen': p.canteen.name,
                    'description': p.description
                }
                response_data['food'].append(food_data)
            response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
            # print "after encoding", type(response_data), response_data

        return HttpResponse(response_data, content_type='text/json')
    return HttpResponse('error')

def order(request):
    print "client.order"
    if request.method == 'POST':
        response_data = {
            'response': 'succeed',
            'STATIC_URL': settings.STATIC_URL,
            'order': []
        }

        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)
        if 'order' in data:
            order_id = data['order']
            order_list = list(models.OrderModel.objects.filter(user=user.id, id=order_id))
            if order_list:
                order_object = order_list.pop()
                basket_list = list(models.BasketModel.objects.filter(order=order_object))
                if not basket_list:
                    return HttpResponse("error")
                food_list = []
                order_price = 0.0
                for basket in basket_list:
                    p = list(models.FoodModel.objects.filter(id=basket.food)).pop()
                    food_data = {
                        'id': p.id,
                        'name': p.name,
                        'price': str(p.price),
                        'img': str(p.img),
                        'canteen': p.canteen.name,
                        'description': p.description
                    }
                    food_list.append(food_data)
                    order_price = order_price + p.price
                food_list.reverse()
                order_object.price = order_price
                order_object.save()
                p = order_object
                order_data = {
                    'id': p.id,
                    'price': str(p.price),
                    'address': p.address,
                    'time': str(p.time)[0:19],
                    'confirm': str(p.confirm),
                    'deal': str(p.deal)
                }
                response_data['order'] = order_data
                response_data['food'] = food_list
        else:
            order_list = list(models.OrderModel.objects.filter(user=user.id))
            for p in order_list:
                order_data = {
                    'id': p.id,
                    'price': str(p.price),
                    'address': p.address,
                    'time': str(p.time)[0:19],
                    'confirm': str(p.confirm),
                    'deal': str(p.deal)
                }
                response_data['order'].append(order_data)
                response_data['order'].reverse()
        response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
        return HttpResponse(response_data, content_type='text/json')

def add_to_order(request):
    print "client method add_to_order", request.POST
    if request.method == 'POST':
        response_data = {
            'response': 'succeed',
            'STATIC_URL': settings.STATIC_URL,
            'order': []
        }

        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)

        if 'food' in data:
            food_id = data['food']
            order_list = list(models.OrderModel.objects.filter(user=user.id, confirm=False))
            if not order_list:
                p = models.OrderModel(
                    user=request.user.id,
                    address='',
                    confirm=False,
                    time=timezone.now()
                )
                p.save()
                order_object = p
            else:
                order_object = order_list.pop()
            p = models.BasketModel(
                order=order_object,
                food=food_id
            )
            p.save()

            basket_list = list(models.BasketModel.objects.filter(order=order_object))
            if not basket_list:
                return HttpResponse("error")
            # food_list = []
            order_price = 0.0
            for basket in basket_list:
                p = list(models.FoodModel.objects.filter(id=basket.food)).pop()
                # food_data = {
                #     'id': p.id,
                #     'name': p.name,
                #     'img': str(p.img),
                #     'canteen': p.canteen.name,
                #     'description': p.description
                # }
                # food_list.append(food_data)
                order_price = order_price + p.price
            # food_list.reverse()
            order_object.price = order_price
            order_object.save()
            p = order_object
            order_data = {
                'id': p.id,
                'price': str(p.price),
                'address': p.address,
                'time': str(p.time)[0:18],
                'confirm': str(p.confirm),
                'deal': str(p.deal)
            }
            response_data['order'] = order_data
            # response_data['food'] = food_list
    else:
        response_data = {
            'response': 'error'
        }
    response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
    return HttpResponse(response_data, content_type='text/json')

def order_confirm(request):
    if request.method == 'POST':
        response_data = {
            'response': 'succeed'
        }
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)
        order_id = data['order_id']
        order_address = data['address']
        order = list(models.OrderModel.objects.filter(id=order_id, user=user.id)).pop()
        order.address = order_address
        order.confirm = True
        order.save()
        response_data = json.dumps(response_data, encoding='utf-8', ensure_ascii=False)
        return HttpResponse(response_data, content_type='text/json')