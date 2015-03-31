from django.shortcuts import render
from django.views import generic

# Create your views here.


class IndexView(generic.View):
    template_name = 'order/templates/index.html'

    def get(self, request):

        temp_text = "Hello"
        context = {
            'temp_text': temp_text,
            'a': 1123
        }
        return render(
            request,
            self.template_name,
            context
        )