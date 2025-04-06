from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Product
from store.serializers import ProductSerializer

# Create your views here.
class AllProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)