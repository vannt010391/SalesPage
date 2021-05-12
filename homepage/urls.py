from django.urls import path
from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('premium', views.premium, name='premium'),
    path('product', views.product, name='product'),
    path('productdetail', views.productdetail, name='productdetail'),
    path('login', views.mylogin, name='login'),
    path('register', views.register, name='register'),
    
]
