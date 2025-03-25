from django.contrib import admin
from .models import Category, Product, Order, Review, Payment

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Payment)
