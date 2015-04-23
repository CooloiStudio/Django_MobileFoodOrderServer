#coding=utf-8
__author__ = 'esoragoto'

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User

from models import Canteen
from forms import CanteenForm
from data import ProjectInfo
from MobileFoodOrderServer import settings


class CanteenView(generic.View):
    template_name = 'order/templates/canteen.html'

    def get(self, request):
        url_name = 'canteen'
        html_title = "食堂中心"
        form = CanteenForm()

        canteen_list = list(Canteen.objects.all())
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
            'url_name': url_name,
            'form': form,
            'canteen_list': canteen_list,
            'STATIC_URL': settings.STATIC_URL
        }
        return render(
            request,
            self.template_name,
            context
        )

def create(request):
    form = CanteenForm(request.POST, request.FILES)
    if form.is_valid():
        canteen = Canteen(
            name=request.POST['name'],
            img=request.FILES['img'],
            description=request.POST['description']
        )
        print canteen
        canteen.save()
    return HttpResponseRedirect(reverse('canteen'))