#coding=utf-8
__author__ = 'esoragoto'

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User

from models import FoodModel, CanteenModel, OrderModel, BasketModel
from forms import FoodForm
import data
from MobileFoodOrderServer import settings

# @login_required(login_url='/login')
class OrderView(generic.View):
    template_name = 'order/templates/order.html'
    url_name = "order"
    html_title = "订单中心"

    context = {
        'html_title': html_title,
        'pro': data.ProjectInfo.data,
        'url_name': url_name
    }

    def food(self, request):
        print "food method"
        if request.user.is_superuser:
            return
        food = request.GET['food']
        order = list(OrderModel.objects.filter(user=request.user.id, confirm=False))
        if not order:
            p = OrderModel(
                user=request.user.id,
                address='',
                confirm=False,
                time=timezone.now()
            )
            p.save()
            order = p
        else:
            order = order.pop()
        p = BasketModel(
            order=order,
            food=food
        )
        p.save()
        self.getorderinfo(order)

    def order(self, request):
        print "oreder method"
        if request.user.is_superuser:
            order = list(OrderModel.objects.filter(id=request.GET['order'], confirm=True))
        else:
            order = list(OrderModel.objects.filter(id=request.GET['order'], user=request.user.id))

        if not order:
            return HttpResponse('error')

        order = order.pop()
        self.getorderinfo(order)

    def getorderinfo(self, order):
        basket_list = list(BasketModel.objects.filter(order=order))
        food_list = []
        order_price = 0.0
        for basket in basket_list:
            p = list(FoodModel.objects.filter(id=basket.food.id))
            food_list = food_list + p
            order_price = order_price + p.pop().price
        food_list.reverse()
        order.price = order_price
        order.save()
        self.context['order'] = order
        self.context['food_list'] = food_list

    method = {
        'food': food,
        'order': order
    }

    def get(self, request):

        if request.GET:
            self.method[list(request.GET).pop()](self, request)

        if request.user.is_superuser:
            order_list = list(OrderModel.objects.filter(confirm=True))
        else:
            order_list = list(OrderModel.objects.filter(user=request.user.id))
        order_list.reverse()
        self.context['order_list'] = order_list
        return render(
            request,
            self.template_name,
            self.context
        )

def deal(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = list(OrderModel.objects.filter(id=order_id)).pop()
        if order.confirm:
            order.deal = True
            order.save()
        return HttpResponseRedirect(reverse('order'))
    if request.method == 'GET':
        return HttpResponse("error")

    return HttpResponse("None")

def confirm(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order_address = request.POST['address']
        order = list(OrderModel.objects.filter(id=order_id)).pop()
        order.address = order_address
        order.confirm = True
        order.save()
        return HttpResponseRedirect(reverse('order'))
    return HttpResponse("None")