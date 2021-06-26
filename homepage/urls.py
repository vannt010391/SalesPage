from django.urls import path
from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('premium', views.premium, name='premium'),
    path('product', views.product, name='product'),    
    path('product/<int:categoryid>/', views.productcategory, name="productcategory"),
    path('<int:id>/detail/', views.productdetail, name='productdetail'),
    path('login', views.mylogin, name='login'),
    path('register', views.register, name='register'),
    path('reply',views.reply,name='reply'),
    path('blog', views.blog, name='blog'),
    path('feedback',views.feedback, name= 'feedback'),    
    path('blog/<int:id>', views.post),
    path('blogcategory/<int:id>', views.blogcategory, name='blogcategory'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

]
