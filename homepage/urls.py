from django.urls import path
from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('premium', views.premium, name='premium'),
    path('product', views.product, name='product'),       
    path('<int:id>/detail/', views.productdetail, name='productdetail'),
    path('login', views.mylogin, name='login'),
    path('register', views.register, name='register'),
    path('reply',views.reply,name='reply'),
    path('searchproduct/',views.SearchViewProduct.as_view(), name='searchproduct'),
    path('searchpremium/',views.SearchViewPremium.as_view(), name='searchpremium'),
]
