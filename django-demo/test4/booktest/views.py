from django.shortcuts import render
from .models import *


def index(request):

    hero = HeroInfo.objects.all()
    context = {'hero': hero}
    return render(request, 'booktest/index.html',context)
