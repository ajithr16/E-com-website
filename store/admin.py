from django.contrib import admin

from .models import Category, Product

# Register your models here.

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price','in_stock','Created','Updated']
    list_filter = ['in_stock','in_active']
    prepopulated_fields = {'slug':('title',)}