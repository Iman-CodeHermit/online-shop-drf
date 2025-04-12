from rest_framework import serializers
from .models import Product, Category, Wish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'

