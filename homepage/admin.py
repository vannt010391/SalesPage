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
    list_display = ("productcategoryid","productcategoryname", "parentcategoryid", "categorylevel", "createdate" )

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


# admin.site.register(BlogCategory)
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("blogcategoryid", "parentid", "displayorder", "name", "createdate", "metaKeywords")

# admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("blogcategoryid", "blogid", "title" ,"blogimage", "metaKeywords", "tagid")  

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

