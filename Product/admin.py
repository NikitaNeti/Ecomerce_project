from django.contrib import admin
from .models import Category,Product
from mptt.admin import MPTTModelAdmin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug' )



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


admin.site.register(Category, MPTTModelAdmin )
admin.site.register(Product, ProductAdmin)
