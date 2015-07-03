#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import json

from myWeather.models import User
    


def index(request):
    if request.method == "POST":
        return HttpResponse("name")
    return HttpResponse(u"lqcshishagua")



# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()
    
@csrf_protect
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #写入数据库
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
        return HttpResponse('upload ok!')
    else:
        uf = UserForm()
        return render_to_response('register.html',{'uf':uf},context_instance=RequestContext(request))

def test(request):

    response_data = {}  
    if request.method == "POST":
        req = simplejson.loads(request.raw_post_data)
        username = req['name']
        headImg = req['fStream']

         #写入数据库
        user = User()
        user.username = username
        user.headImg = headImg 
        user.save()

    return HttpResponse('upload ok!')



def image(request):
    if request.method == "POST":
        name = request.POST.get('name',1) 
        print(name)
        #写入数据库
        user = User()
        user.username = username
        #user.headImg = headImg 
        user.save()
        return HttpResponse("tname")

    return HttpResponse(u"lqcshishagua")
