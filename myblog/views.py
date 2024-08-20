from django.shortcuts import render,get_object_or_404,redirect
from . import models

from . import forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
def homepage(request):
    bloglar = models.Blogs.objects.all()
    return render(request,'home.html',{'postlar':bloglar})


def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'reg.html',{'form':form})

def sing_in(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})


def log_out(request):
    logout(request)
    return redirect('home')


def detail(request,id):
    post = get_object_or_404(models.Blogs,id=id)
    return render(request,'detail.html',{'post':post})
