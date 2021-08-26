from django.urls import path
from . import views
from . views import HomePage

urlpatterns =[
    path('', views.HomePage, name="Home"),
]