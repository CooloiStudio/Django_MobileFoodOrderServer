#coding=utf8

from django.shortcuts import render
from django.views import generic

from models import ProjectInfo

# Create your views here.


class IndexView(generic.View):
    template_name = 'order/templates/index.html'

    def get(self, request):

        html_title = "Homepage"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
        }
        return render(
            request,
            self.template_name,
            context
        )

class UserView(generic.View):
    template_name = 'order/templates/user.html'

    def get(self, request):

        html_title = "User"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
        }
        return render(
            request,
            self.template_name,
            context
        )

class OrderView(generic.View):
    template_name = 'order/templates/order.html'

    def get(self, request):

        html_title = "Order"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
        }
        return render(
            request,
            self.template_name,
            context
        )

class InfoView(generic.View):
    template_name = 'order/templates/info.html'

    def get(self, request):

        html_title = "Info"
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
        }
        return render(
            request,
            self.template_name,
            context
        )