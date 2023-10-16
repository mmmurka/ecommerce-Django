from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
# Create your views here.

def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = category_page.product_set.filter(available=True)
    else:
        products = Product.objects.filter(available=True)
    return render(request, 'home.html', {'category': category_page, 'products': products})

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    return render(request, 'product.html', {'product': product})


def cart(request):
    return render(request, 'cart.html')