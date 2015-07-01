#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from myWeather.models import User
    


#def index(request):
 #   return HttpResponse(u"hello!")

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
