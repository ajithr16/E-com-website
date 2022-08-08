from distutils.command.upload import upload
from tabnanny import verbose
from turtle import title
from unicodedata import category

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self) :
        return self.name



    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-Created',)

    def get_absolute_url(self):
        return reverse('store:product_details', args=[self.slug])
        



    def __str__(self):
        return self.title