from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=250, blank=True, null=True)
    password = models.CharField(max_length=32, blank=False, null = False)
    address = models.TextField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='account/', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'Account'


class ProductCategory(models.Model):
    productcategoryid = models.AutoField(primary_key=True)
    productcategoryname = models.CharField(max_length=100)
    metatitle = models.CharField(max_length=250, blank=True, null=True)
    parentcategoryid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentCategoryId', blank=True, null=True) 
    displayoder = models.IntegerField(blank=True, null=True)
    SEOtitle = models.TextField(max_length=100, blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    editeddate = models.DateTimeField(auto_now=True, blank=True, null=True)
    metaKeywords = models.TextField(max_length=250,blank=True, null=True)
    metaDescriptions = models.TextField(max_length=250,blank=True, null=True)
    isenable = models.BooleanField(blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'ProductCategory'

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    productcategoryid = models.ForeignKey(ProductCategory, models.CASCADE, blank=True, null=True)
    productcode = models.CharField(max_length=50, blank=True, null=True)
    productname = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)
    metatitle = models.TextField(blank=True, null=True)
    descriptions = RichTextUploadingField(blank=True, null=True)
    productimage = models.ImageField(upload_to='product/')
    moreimage = models.ImageField(upload_to='productdetail/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    promotionprice = models.CharField(max_length=50, blank=True, null=True)
    includeVAT = models.CharField(max_length=150,blank=True, null=True)
    viewcounts = models.IntegerField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    editeddate = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.productname  

    class Meta:
        managed = True
        db_table = 'Product'

class BlogCategory(models.Model):
    blogcategoryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    metatitle = models.CharField(max_length=250, blank=True, null=True)
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)
    displayorder = models.IntegerField(blank=True, null=True)
    SEOtitle = models.CharField(max_length=250, blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    editeddate = models.DateTimeField(auto_now=True, blank=True, null=True)
    metaKeywords = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'BlogCategory'


class Blog(models.Model):
    blogid = models.AutoField(primary_key=True)
    blogcategoryid = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    title = models.TextField(max_length=100, blank=True, null=True)
    metatitle = models.TextField(max_length=250, blank=True, null=True)
    description =  RichTextUploadingField(blank=True, null=True)
    blogimage = models.ImageField(upload_to='news/')
    details = RichTextUploadingField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    editeddate = models.DateTimeField(auto_now=True, blank=True, null=True)
    metaKeywords = models.CharField(max_length=250, blank=True, null=True)
    metaDescriptions = models.CharField(max_length=250, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    isenable = models.BooleanField(blank=True, null=True)
    viewcount = models.IntegerField(blank=True, null=True)
    tagid = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        managed = True
        db_table = 'Blog'

class Footer(models.Model):
    footerid = models.AutoField(primary_key=True)
    content = RichTextUploadingField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Footer'

class Tag(models.Model):
    tagid = models.AutoField(primary_key=True)
    tagname = models.TextField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tag'

class BlogTag(models.Model):
    blogtagid = models.AutoField(primary_key=True)
    tagid = models.ForeignKey(Tag, on_delete=models.CASCADE)
    blogtagname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'BlogTag'


class About(models.Model):
    aboutid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    metatitle = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='about/')
    detail = RichTextUploadingField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    editeddate = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'About'

class Contact(models.Model):
    contactid = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Contact'

class Feedback(models.Model):
    feedbackid = models.AutoField(primary_key=True)
    namefeedback = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True, blank=True, null=True)
    createdate = models.DateTimeField(blank=True, null=True)
    note = models.TextField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Feedback'

class Slide(models.Model):
    slideid = models.AutoField(primary_key=True)
    slidename = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slide/')
    displayorder = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    editeddate = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.slidename

    class Meta:
        managed = True
        db_table = 'Slide'

STATUS_CHOICES = (
    ('ORDER', 'ĐẶT HÀNG'),
    ('CONFIRM', 'XÁC NHẬN'),
    ('DELIVERING', 'ĐANG VẬN CHUYỂN'),
    ('COMPLETED', 'HOÀN TẤT')
)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=0)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    startdate = models.DateTimeField(auto_now_add=True)
    ordereddate = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    shippingaddress = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    completeddate = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.user.username

    