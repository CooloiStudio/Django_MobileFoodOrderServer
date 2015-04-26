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

    def food(request):
        print "food method"
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
        basket_list = list(BasketModel.objects.filter(order=order))
        food_list = []
        order_price = 0
        for basket in basket_list:
            p = list(FoodModel.objects.filter(id=basket.food))
            food_list = food_list + p
            order_price = order_price + p.pop().price
        order.price = order_price
        order.save()
        food_mothed_data = {
            'order': order,
            'food_list': food_list
        }
        return food_mothed_data

    def order(request):
        print "oreder method"
        # print request.GET['order']
        return 0

    def basket(request):
        print "basket method"
        if 'baseket' in list(request.GET):
            return 0
        return 0
    method = {
        'food': food,
        'order': order,
        'basket': basket
    }
    def get(self, request):
        url_name = "order"
        html_title = "订单中心"

        order_list = list(OrderModel.objects.filter(user=request.user.id))
        context = {
            'html_title': html_title,
            'pro': data.ProjectInfo.data,
            'url_name': url_name,
            'order_list': order_list
        }
        if request.GET:
            method_data = self.method[list(request.GET).pop()](request)
            context = dict(context.items() + method_data.items())
        return render(
            request,
            self.template_name,
            context
        )

def create(request):
    if request.method == 'GET':
        return HttpResponse("error")

    return HttpResponse("None")