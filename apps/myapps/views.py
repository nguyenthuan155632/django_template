from django.shortcuts import render
from django.views import generic
from .models import Myapps

# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'myapps'
    template_name = 'myapps/index.html'

    def get_queryset(self):
        return Myapps.objects.all()


class DetailView(generic.DetailView):
    model = Myapps
    template_name = 'myapps/detail.html'
