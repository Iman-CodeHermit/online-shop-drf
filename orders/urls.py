from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name="cart"),
    path('cart/remove/<int:item_id>/', views.CartItemDeleteView.as_view(), name="cart-remove"),
    path('checkout/', views.CheckoutView.as_view(), name="checkout"),
]