from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, Order, OrderItem
from .serializers import CartSerializer, OrderSerializer


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))
        item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        if not created:
            item.quantity += quantity
            item.save()
        return Response({"message": "Product added to cart"}, status=status.HTTP_201_CREATED)

class CartItemDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        cart = Cart.objects.get(user=request.user)
        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
            item.delete()
            return Response({"message": "Product removed from cart"}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        if not cart.items.exists():
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user, total_amount=cart.total_price())

        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity,
                                     price=item.total_price())

        cart.items.all().delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)



