from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.AllProductsView.as_view(), name='all-products'),
]