from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('categories-detail/', views.CategoryDetailView.as_view(), name='categories-detail'),
    path('product-detail/', views.ProductsDetailView.as_view(), name='product-detail'),
    path('product=search/', views.ProductSearchView.as_view(), name='product-search'),
    path('wish/', views.WishListView.as_view(), name='wish-list')
]
