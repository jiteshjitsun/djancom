from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Home/home.html', context)

def cart(request):
    context = {}
    return render(request, 'Home/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'Home/checkout.html', context)