from django.core.serializers import serialize
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category, Wish
from .serializers import CategorySerializer, ProductSerializer, WishListSerializer
from rest_framework import filters

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name']

class WishListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        wishlist = Wish.objects.filter(user=request.user)
        serializer = WishListSerializer(wishlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.data.get('product')
        product = Product.objects.get(id=product_id)

        if Wish.objects.filter(user=request.user, product=product).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        wishlist_item = Wish.objects.create(user=request.user, product=product)
        serializer = WishListSerializer(wishlist_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

     def delete(self, request):
         product_id = request.data.get('product')
         wishlist_item = Wish.objects.filter(user = request.user, product_id=product_id).first()

         if not wishlist_item:
             return Response(status=status.HTTP_404_NOT_FOUND)
         wishlist_item.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
