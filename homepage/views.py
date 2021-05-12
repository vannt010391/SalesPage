from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from homepage.models import *
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User



# Create your views here.

def index(request):
   
    return render(request, 'homepage/index.html')
    
def about(request):
    return render(request,'homepage/about.html')

def blog(request):
    return render(request,'homepage/blog.html')

def contact(request):
    return render(request,'homepage/contact.html')

def mylogin(request):
    return render(request,'homepage/login.html')



def register(request):
    return render(request,'homepage/register.html')

def premium(request):
    return render(request,'homepage/premium.html')

def product(request):
    return render(request,'homepage/product.html')
    
def productdetail(request):
    return render(request, 'homepage/productdetail.html')



    


