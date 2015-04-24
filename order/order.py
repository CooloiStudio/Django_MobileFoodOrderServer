#coding=utf-8
__author__ = 'esoragoto'

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User

from models import FoodModel, CanteenModel, OrderModel
from forms import FoodForm
import data
from MobileFoodOrderServer import settings

# @login_required(login_url='/login')
class OrderView(generic.View):
    template_name = 'order/templates/order.html'

    def get(self, request):
        url_name = "order"
        html_title = "订单中心"
        context = {
            'html_title': html_title,
            'pro': data.ProjectInfo.data,
            'url_name': url_name,
        }
        return render(
            request,
            self.template_name,
            context
        )