from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'Home/home.html', context)

def cart(request):
    context = {}
    return render(request, 'Home/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'Home/checkout.html', context)