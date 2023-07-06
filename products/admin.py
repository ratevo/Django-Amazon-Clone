from django.contrib import admin
from .models import Product , ProductImages , Brand , Review


# Register your models here.



# change img in line admin panel
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 3





# Admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','quantity','price']
    list_filter = ['price','quantity','brand','tags']
    search_fields = ['name','subtitle','description']
    inlines = (ProductImagesInline,)
    summernote_fields = '__all__'




# >>start

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)