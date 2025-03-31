from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category, Wish
from .serializers import CategorySerializer, ProductSerializer, WishListSerializer

# Create your views here.
class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductsView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductsDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductSearchView(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', '')
        product = Product.objects.filter(name__icontains=search_query) | Product.objects.filter(category__name__incontains=search_query)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
