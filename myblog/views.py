from django.shortcuts import render,get_object_or_404
from . import models



def homepage(request):
    bloglar = models.Blogs.objects.all()
    return render(request,'home.html',{'postlar':bloglar})
