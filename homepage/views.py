from typing import Generic
import homepage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import admin,messages
from django.urls import path, include
from homepage.models import *
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from django import forms
# Create your views here.

def index(request):
    products = Product.objects.all()
    slides = Slide.objects.all()
    return render(request, 'homepage/index.html', {'slides':slides , 'products':products })
    
    
def about(request):
    return render(request,'homepage/about.html')

def blog(request):
    return render(request,'homepage/blog.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if re.match(r'^\w+$', name):
            if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
                obj=Contact()
                obj.name=name
                obj.email=email
                obj.messages=message
                obj.save()
                messages.info(request,"cảm ơn phản hồi của bạn")
            else:
                print(1)
                messages.info(request,"Email của bạn không hợp lệ")
        else:
            print(2)
            messages.SUCCESS(request,"tên của bạn không hợp lệ")

        
    return render(request,'homepage/contact.html')

def mylogin(request):
    return render(request,'homepage/login.html')

def register(request):
    return render(request,'homepage/register.html')

# def premium(request):
#     productcategory_list = ProductCategory.objects.all()
#     # Paging
#     paginator = Paginator(productcategory_list, 5)
#     page = request.GET.get('page', 1)
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)

#     context = {
#         "page_obj": products
#     }
#     return render(request,'homepage/premium.html')

def product(request):
    productcategory_list = ProductCategory.objects.all()
    product_list = Product.objects.all()

    # Paging
    paginator = Paginator(product_list, 20)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'productcategory_list': productcategory_list,
        "page_obj": products
    }
    return render(request,'homepage/product.html', context)
# Chị Vân demo
def premium(request):
    products = Product.objects.filter(productcategoryid=4)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'homepage/premium.html',{'products':products, 'page_obj': page_obj})

class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'homepage/productdetail.html'

class SearchView(generic.ListView):
    model = Product
    template_name = 'homepage/product.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Product.objects.filter(productname__contains=query)
          result = postresult
       else:
           result = None
       return result

def reply(request):
    return render(request,'homepage/reply.html')

    


