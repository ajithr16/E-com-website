from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock = True)
    return render(request,'store/products/details.html', {'product':product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)   
    products = Product.objects.filter(category= category)
    return render(request,'store/products/category.html',{'category':category, 'products':products}) 


def all_products(request):
    products = Product.objects.all() #selectquery on products
    return render(request,'store/home.html',{'products':products})