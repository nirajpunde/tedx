# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
def home(request):
    context={}
    return render(request,'home.html',context)

def contact_us(request):
    context={}
    return render(request,"contact_us.html",context)

def about_us(request):
    context={}
    return render(request,"page3.html",context)

def ted_com(request):
    context={}
    return render(request,"ted_com.html",context)
