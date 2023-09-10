from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.

def Setcookie(request):
    response=render(request,'student/setcookies.html')
    # response.set_cookie('name','sarvesh',max_age=60)
    # response.set_cookie('name','sarvesh',expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie('name','sarvesh',salt='nm',expires=datetime.utcnow()+timedelta(days=2))

    return response


def Getcookie(request):
    # name=request.COOKIES['name']
    # name=request.COOKIES.get('name')
    # name=request.COOKIES.get('name','guest')
    name=request.get_signed_cookie('name','guest',salt='nm')
    return render(request,'student/getcookies.html',{'name':name})

def Deletecookie(request):
    response=render(request,'student/deletecookies.html')
    response.delete_cookie('name')
    return response