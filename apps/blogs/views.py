from django.shortcuts import render
from .models import *
from django.conf import settings

# Create your views here.

def index(request):
    template_name = 'blogs/index.html'
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, template_name, context)
