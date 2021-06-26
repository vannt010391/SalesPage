from typing import Generic
from django.core.exceptions import ValidationError
from django.http import response
from collections import Counter
from django.http.response import HttpResponseRedirect
import homepage
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404, redirect
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
from homepage.extras import generate_order_id
from django.urls import reverse

def index(request):
    products = Product.objects.all()
    slides = Slide.objects.all()
    return render(request, 'homepage/index.html', {'slides':slides , 'products':products })
    
    
def about(request):
    return render(request,'homepage/about.html')

def blog(request):
    blogcategorylist = BlogCategory.objects.all() 
    blogs = Blog.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Blog.objects.filter(metaKeywords__icontains=q)
    else:
        posts=Blog.objects.all().order_by("-createdate")
    cateParents = BlogCategory.objects.filter(parent_id=0)
    # Pagintion
    paginator=Paginator(posts,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context = {
        'blogcategorylist': blogcategorylist,
        'page_obj':page_obj,
        'blogs' : blogs,
        'parents':cateParents
        
    }
    return render(request,'homepage/blog.html', context)


def blogcategory(request, id):
    blogcategorylist = BlogCategory.objects.all() 
    cateParents = BlogCategory.objects.filter(parent_id=0)
    blogs = Blog.objects.filter(blogcategoryid=id)
    context = {
        'blogcategorylist': blogcategorylist,
        'page_obj' : blogs,
        'parents':cateParents
    }
    return render(request, 'homepage/blog.html', context)


def post(request,id):
    post = Blog.objects.get(blogid = id)
    blogs = post.blogcategoryid
    relateblog = Blog.objects.filter(blogcategoryid=blogs)
    context =  {
        'post' : post,
        'relateblog' : relateblog,
    }
    return render(request, 'homepage/post.html', context)
    

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['messages']
            date = timezone.now()
            obj=Contact()
            obj.date=date
            obj.name=name
            obj.email=email
            obj.messages=message
            obj.save()
            contact ={'message': 'Cảm ơn phản hồi của bạn'}
            return render(request,'homepage/feedback.html',contact)
            #messages.success(request,"Cảm ơn phản hồi của bạn"
    context={'form' :form}
    return render(request,'homepage/contact.html',context)

def feedback(request):
    return render(request,'homepage/feedback.html',contact)

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
    productcategory_list = ProductCategory.objects.filter(isenable__exact=True)

    url_parameter = request.GET.get("search")
    if url_parameter:
        products = Product.objects.filter(productname__icontains=url_parameter)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  

    context = {
        'productcategory_list': productcategory_list,
        'products': products,
        'page_obj': page_obj,
    }

    return render(request,'homepage/product.html', context)

def productcategory(request, categoryid):
    productcategory_list = ProductCategory.objects.filter(isenable__exact=True)
    category = ProductCategory.objects.get(productcategoryid=categoryid).productcategoryname
    products = Product.objects.filter(productcategoryid=categoryid)
    url_parameter = request.GET.get("search")
    if url_parameter:
        products = Product.objects.filter(productname__icontains=url_parameter)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  

    context = {
        'productcategory_list': productcategory_list,
        'category': category,
        'products': products,
        'page_obj': page_obj,
    }
    return render(request,'homepage/product.html', context)

# Chị Vân demo
def premium(request):
    products = Product.objects.filter(productcategoryid=4)
    url_parameter = request.GET.get("search")
    if url_parameter:
        products = products.filter(productname__icontains=url_parameter)    
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'page_obj': page_obj,
    }
    return render(request,'homepage/premium.html', context)

def productdetail (request, id):
    product = Product.objects.get(productid=id)
    relatedproducts = Product.objects.filter(productcategoryid=product.productcategoryid)
    context = {
        'product': product,
        'relatedproducts': relatedproducts,
    }
    return render(request, 'homepage/productdetail.html', context)

def reply(request):
    return render(request,'homepage/reply.html')

def new_func(email):
    print(email)

def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Account, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product-list')) 
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('products:product-list'))   


