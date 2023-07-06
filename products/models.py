from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 


# Create your models here.





# Product Start 
class Product(models.Model):

    name = models.CharField(max_length=120)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=30000)
    subtitle = models.TextField(max_length=500)
    sku = models.IntegerField()
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
      tags = TaggableManager()

    def __str__(self):
        return self.name




# Products Images Start

class ProductImages(models.Model):
    Product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productiamges')


    def __str__(self):
        return str(self.product)
    






# Images End











# Brand start
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands')


    def __str__(self):
        return self.name

#  Product End


# Review Start

class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    reviw = models.TextField(max_length=500)
    rate = models.IntegerField() 
    create_date = models.DateTimeField(default=timezone.now)





def __str__(self):
    return str(self.product)