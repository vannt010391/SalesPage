from typing import Generic, Reversible
from django import views
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import message
from django.http import request
from collections import Counter
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.base import View
import homepage
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, include
from homepage.models import *
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *
from .sendmail import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import uuid
from django.utils import timezone
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetConfirmView

# Create your views here.

def index(request):
    products = Product.objects.all()
    slides = Slide.objects.all()
    return render(request, 'homepage/index.html', {'slides': slides, 'products': products})


def about(request):
    return render(request, 'homepage/about.html')


def blog(request):
    return render(request, 'homepage/blog.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['messages']
            date = timezone.now()
            obj = Contact()
            obj.date = date
            obj.name = name
            obj.email = email
            obj.messages = message
            obj.save()
            contact = {'message': 'Cảm ơn phản hồi của bạn'}
            return render(request, 'homepage/feedback.html', contact)
            # messages.success(request,"Cảm ơn phản hồi của bạn"
    context = {'form': form}
    return render(request, 'homepage/contact.html', context)


def feedback(request):
    return render(request, 'homepage/feedback.html', contact)


class mylogin(LoginView):
    template_name = 'homepage/login.html'


class EditLogin(LoginRequiredMixin, TemplateView):
    template_name = 'homepage/profile.html'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="Có ít nhất 8 kí tự bao gồm cả số và chữ",
    )

    class Meta:
        model = User
        fields = ("email", "username",)
        field_classes = {'username': UsernameField}


class SiteRegisterView(FormView):
    template_name = 'homepage/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email'])
        url = f"{reverse('homepage:login')}?username={new_user.username}"

        return redirect(url)

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name ='homepage/password_confirm.html'


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

    return render(request, 'homepage/product.html', context)


def productcategory(request, categoryid):
    productcategory_list = ProductCategory.objects.filter(isenable__exact=True)
    category = ProductCategory.objects.get(
        productcategoryid=categoryid).productcategoryname
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
    return render(request, 'homepage/product.html', context)

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
    return render(request, 'homepage/premium.html', context)


def productdetail(request, id):
    product = Product.objects.get(productid=id)
    relatedproducts = Product.objects.filter(
        productcategoryid=product.productcategoryid)
    context = {
        'product': product,
        'relatedproducts': relatedproducts,
    }
    return render(request, 'homepage/productdetail.html', context)


def reply(request):
    return render(request, 'homepage/reply.html')


def new_func(email):
    print(email)
