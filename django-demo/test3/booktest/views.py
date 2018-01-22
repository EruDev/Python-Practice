# coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def index(request):

    return HttpResponse('hello world')


def detail(request,p1,p2,p3):

    return HttpResponse('year:%s month:%s day:%s' % (p1, p2, p3))

# get练习
def gettest1(request):

    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1, 'b':b1, 'c': c1}
    return render(request, 'booktest/gettest1.html', context)


def gettest2(request):

    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1, 'b':b1, 'c': c1}
    return render(request, 'booktest/gettest2.html', context)


def gettest3(request):

    a = request.GET.getlist('a')
    b = request.GET['b']
    context = {'a':a, 'b':b}
    return render(request, 'booktest/gettest3.html', context)

# post练习
def posttest1(request):

    return render(request, 'booktest/posttest1.html')


def posttest2(request):

    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'booktest/posttest2.html', context)

# cookie练习
def cookietest(request):

    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('c1'):
        response.write(cookie['c1'])
    # response.set_cookie('h1', '你好')

    return response

# redirect练习
def redtest1(request):

    return redirect('/booktest/redtest2/')


def redtest2(request):

    return HttpResponse('这是转向的页面')


# 通过用户登录练习session
def session1(request):

    uname = request.session.get('myname', '未登录')
    context = {'uname': uname}
    return render(request, 'booktest/session1.html', context)

def session2(request):
    return render(request, 'booktest/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect('/booktest/session1/')

def session3(request):
    # 删除session
    del request.session['myname']
    return redirect('/booktest/session1/')