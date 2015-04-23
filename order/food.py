#coding=utf-8
__author__ = 'esoragoto'

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User

from models import FoodModel, Canteen
from forms import FoodForm
from data import ProjectInfo
from MobileFoodOrderServer import settings

class FoodView(generic.View):
    template_name = 'order/templates/food.html'

    def get(self, request):
        url_name = 'food'
        html_title = "菜品中心"
        form = FoodForm()

        food_list = list(FoodModel.objects.all())
        context = {
            'html_title': html_title,
            'pro': ProjectInfo.data,
            'url_name': url_name,
            'form': form,
            'food_list': food_list,
            'STATIC_URL': settings.STATIC_URL
        }
        return render(
            request,
            self.template_name,
            context
        )

def create(request):
    form = FoodForm(request.POST, request.FILES)
    if form.is_valid():
        food = FoodModel(
            canteen=Canteen.objects.filter(id=request.POST['canteen'])[0],
            name=request.POST['name'],
            img=request.FILES['img'],
            description=request.POST['description']
        )
        print food
        food.save()
    return HttpResponseRedirect(reverse('food'))