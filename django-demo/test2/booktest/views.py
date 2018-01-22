from django.db.models import F, Q
from django.shortcuts import render
from .models import *


def index(request):

    # list = BookInfo.books1.filter(Q(pk__lt=4)).filter(bcomment__lt=40)
    list = BookInfo.books1.filter(Q(pk__lt=4) | Q(bcomment__lt=40))  # id小于4或者评论小于40
    context = {'list':list}
    return render(request,'booktest/index.html', context)
