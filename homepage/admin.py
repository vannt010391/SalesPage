from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Account)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "fullname", "photo","createdate", "editdate", "isenable")

# admin.site.register(Slide)
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ("slideid", "slidename", "image", "display")

# admin.site.register(ProductCategory)
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("productcategoryid","productcategoryname", "parentcategoryid","createdate" )

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("productid","productcategoryid","productcode", "productname", "productimage")

# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("orderid","user", "ordereddate", "status")

# admin.site.register(OrderItem)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("user", "ordered", "quantity"  )


# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("contactid","email", "name", "messages","status","date",)