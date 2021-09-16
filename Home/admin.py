from django.contrib import admin
from .models import Product,Customer,ShippingAddress,Order,OrderItems

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItems)