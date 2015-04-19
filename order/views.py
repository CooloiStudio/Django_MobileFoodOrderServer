#coding=utf8

from django.shortcuts import render
from django.views import generic

from models import ProjectInfo

# Create your views here.


class IndexView(generic.View):
    template_name = 'order/templates/index.html'

    def get(self, request):

        url_name = "home"
        html_title = "Homepage"
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

class UserView(generic.View):
    template_name = 'order/templates/user.html'

    def get(self, request):

        url_name = "user"
        html_title = "User"
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

class OrderView(generic.View):
    template_name = 'order/templates/order.html'

    def get(self, request):

        url_name = "order"
        html_title = "Order"
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
        html_title = "Info"
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