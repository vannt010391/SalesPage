
from django.urls import path, include
from homepage import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
app_name = 'homepage'

urlpatterns = [
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('premium', views.premium, name='premium'),
    path('product', views.product, name='product'),    
    path('product/<int:categoryid>/', views.productcategory, name="productcategory"),
    path('<int:id>/detail/', views.productdetail, name='productdetail'),
    path('register', views.SiteRegisterView.as_view(), name='register'),
    path('reply',views.reply,name='reply'),
    path('blog', views.blog, name='blog'),
    path('feedback',views.feedback, name= 'feedback'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', views.mylogin.as_view(), name='login'),
    path('accounts/profile/', views.EditLogin.as_view(), name='profile'),
    path('password_reset',
        auth_views.PasswordResetView.as_view(
            template_name = 'homepage/reset_password.html'
        ),
        name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            
        ),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',views.PasswordResetConfirm.as_view(),
        name='password_reset_confirm')
    

]
