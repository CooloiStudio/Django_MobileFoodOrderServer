#coding=utf8

from django.shortcuts import render
from django.views import generic

# Create your views here.


class IndexView(generic.View):
    template_name = 'order/templates/index.html'

    def get(self, request):

        html_title = "Hello"
        html_title_cn = "您好"
        # context = {
        #     'html_title': html_title,
        # }
        context = {
            'html_title': html_title_cn,
        }
        return render(
            request,
            self.template_name,
            context
        )