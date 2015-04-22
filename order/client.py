__author__ = 'esoragoto'

#coding=utf-8

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User

import json

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
