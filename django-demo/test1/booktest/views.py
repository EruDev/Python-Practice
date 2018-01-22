from django.http import *
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import BookInfo


def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())

    book_list = BookInfo.objects.all()
    context = {'list':book_list}
    return render(request, 'booktest/index.html', context=context)


def show(request, id):

    book = BookInfo.objects.get(pk=id)
    heroList = book.heroinfo_set.all()
    context = {'list':heroList}
    return render(request,'booktest/show.html',context)
