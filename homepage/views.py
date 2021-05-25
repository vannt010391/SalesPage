from typing import Generic
import homepage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from homepage.models import *
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
   
    return render(request, 'homepage/index.html')
    
def about(request):
    return render(request,'homepage/about.html')

def blog(request):
    return render(request,'homepage/blog.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        obj=Contact()
        obj.name=name
        obj.email=email
        obj.messages=message
        obj.save()
    return render(request,'homepage/contact.html')

def mylogin(request):
    return render(request,'homepage/login.html')

def register(request):
    return render(request,'homepage/register.html')

def premium(request):
    productcategory_list = ProductCategory.objects.all()
    # Paging
    paginator = Paginator(productcategory_list, 5)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "page_obj": products
    }
    return render(request,'homepage/premium.html')

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

    


