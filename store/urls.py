from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductsViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
