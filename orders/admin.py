from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

# Register your models here.
admin.site.regiter(Cart)
admin.site.regiter(CartItem)
admin.site.regiter(Order)
admin.site.regiter(OrderItem)
