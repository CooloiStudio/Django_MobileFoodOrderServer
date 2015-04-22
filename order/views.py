#coding=utf-8

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User

from models import ProjectInfo

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


# Create your views here.


class IndexView(generic.View):
    template_name = 'order/templates/index.html'

    def get(self, request):

        url_name = "home"
        html_title = "老干爹订餐"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
            'url_name': url_name,
        }
        return render(
            request,
            self.template_name,
            context
        )

class RegistView(generic.View):
    template_name = 'order/templates/regist.html'

    def get(self, request):
        url_name = "regist"
        html_title = "注册中心"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
            'url_name': url_name,
        }
        return render(
            request,
            self.template_name,
            context
        )

# @login_required(login_url='/login')
class OrderView(generic.View):
    template_name = 'order/templates/order.html'

    def get(self, request):
        url_name = "order"
        html_title = "订单中心"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
            'url_name': url_name,
        }
        return render(
            request,
            self.template_name,
            context
        )

class InfoView(generic.View):
    template_name = 'order/templates/info.html'

    def get(self, request):

        url_name = "info"
        html_title = "信息中心"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
            'url_name': url_name,
        }
        return render(
            request,
            self.template_name,
            context
        )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print username, password
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('info'))

def changepw(request):
    if request.method == 'POST':
        username = request.user.username
        password = request.POST['password']
        newpw = request.POST['newpw']
        user = auth.authenticate(username=username, password=password)
        user.set_password(newpw)
        user.save()
        return HttpResponseRedirect(reverse('info'))
    else:
        return HttpResponseRedirect(reverse('info'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # print username, email, password, is_superuser
        user = User.objects.create_user(username, email, password)
        if request.POST.get('is_superuser') != None:
            user.is_superuser = True
            user.save()
        return HttpResponseRedirect(reverse('info'))
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('regist'))
