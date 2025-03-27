from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductsViewSet
from . import views
router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('wish/', views.WishListView.as_view(), name='wish-list')
]
