from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()