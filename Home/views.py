import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, OrderItem, Product, Order

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Home/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total': 0, 'get_cart_items': 0 }
    context = {'items':items, 'order':order}
    return render(request, 'Home/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total': 0, 'get_cart_items': 0 }
    context = {'items':items, 'order':order}
    return render(request, 'Home/checkout.html', context)

def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False) 

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)

def contactUs(request):
    return render(request, 'Home/contact.html')

def aboutUs(request):
    return render(request, 'Home/about.html')