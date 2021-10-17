from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_cart', views.updateItem, name="update_cart"),
    path('contact/', views.contactUs, name="contact")

]