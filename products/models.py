from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import random



# Create your models here.


FLAGS_TYPES = (
    ('New' , 'New'),
    ('Sale' , 'Sale'),
    ('Feature' , 'Feature'),
)


# Product Start 
class Product(models.Model):

    name = models.CharField(_('name'),max_length=120,)
    price = models.FloatField(_('price'))
    quantity = models.IntegerField(_('quantity'))
    description = models.TextField(_('description'),max_length=30000)
    subtitle = models.TextField(_('subtitle'),max_length=500)
    sku = models.IntegerField(_('sku'))
    brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='products')
    flag = models.CharField(max_length=10, choices=FLAGS_TYPES , default='New')
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs) # Call the real save() method



# Products Images Start

class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='productiamges')


    def __str__(self):
        return str(self.product)
    














# Images End
#  Product End


# Brand start
class Brand(models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brands')
    slug = models.SlugField(null=True,blank=True,unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.name)}{random.randint(1000,100000000)}"
        super(Brand, self).save(*args, **kwargs) # Call the real save() method  

#  Brand End


# Review Start

class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_('user'),related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_review',on_delete=models.CASCADE)
    reviw = models.TextField(_('reviw'),max_length=500)
    rate = models.IntegerField(_('rate')) 
    create_date = models.DateTimeField(_('create_date'),default=timezone.now)





def __str__(self):
    return str(self.product)