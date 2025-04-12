from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'store_order')
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    text = models.TextField()
    rating = models.IntegerField()

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    transaction_id = models.CharField(max_length=256, blank=True, null=True)

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wish')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productwish')

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user} wish {self.product}'
