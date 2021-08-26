from django.shortcuts import render
from .models import Products

# Create your views here.
def HomePage(request):
    product = Products.objects.all()
    return render(request, 'Home/base.html', {'product': product})