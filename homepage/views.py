from typing import Generic
from django.http import response

from django.http.response import HttpResponseRedirect
import homepage
from .forms import ContactForm
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
    form = ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['messages']
            obj=Contact()
            obj.name=name
            obj.email=email
            obj.messages=message
            obj.save()
            return render(request,'homepage/contact.html',{'message': 'Cảm ơn phản hồi của bạn'})
            #messages.success(request,"Cảm ơn phản hồi của bạn"
    context={'form' :form}
    return render(request,'homepage/contact.html',context)

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

    


