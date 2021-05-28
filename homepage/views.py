from typing import Generic
import homepage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from homepage.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def product(request):
    productcategory_list = ProductCategory.objects.all()
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'productcategory_list': productcategory_list,
        'product_list': product_list,
        "page_obj": page_obj
    }
    return render(request,'homepage/product.html', context)

# Chị Vân demo
def premium(request):
    products = Product.objects.filter(productcategoryid=4)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'homepage/premium.html',{'products':products, 'page_obj': page_obj})

def productdetail(request, id):
    product = Product.objects.get(productid=id)
    category = product.productcategoryid
    relatedproduct = Product.objects.filter(productcategoryid=category)
    context = {
        'product': product,
        'relatedproduct': relatedproduct,
    }
    return render(request,'homepage/productdetail.html', context)


class SearchViewProduct(generic.ListView):
    model = Product
    template_name = 'homepage/product.html'
    context_object_name = 'all_search_results'
    paginate_by = 9

    def get_queryset(self):
        result = super(SearchViewProduct, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
           postresult = Product.objects.filter(productname__contains=query)
           result = postresult
        else:
           result = None
        return result

class SearchViewPremium(generic.ListView):
    model = Product
    template_name = 'homepage/premium.html'
    context_object_name = 'all_search_results'
    paginate_by = 9

    def get_queryset(self):
        result = super(SearchViewPremium, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
           postresult = Product.objects.filter(productcategoryid=4,productname__contains=query)
           result = postresult
        else:
           result = None
        return result

def reply(request):
    return render(request,'homepage/reply.html')



