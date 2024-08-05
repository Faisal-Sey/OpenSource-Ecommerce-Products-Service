from typing import Any

from rest_framework import generics

from products.models.products_model import Product, ProductCart
from products.serializers.product_serializer import (
    ProductCartSerializer
)
from utils.logger.logger_handler import logger


class CartListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCart.objects.all()
    serializer_class = ProductCartSerializer

    def get_queryset(self) -> Any:
        logger.debug("Fetching carts list...")
        queryset = super().get_queryset()
        logger.debug("Fetched %d carts items", queryset.count())
        return queryset


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCart.objects.all()
    serializer_class = ProductCartSerializer

    def get_object(self) -> ProductCart:
        cart_id = self.kwargs.get('pk')
        logger.debug("Fetching carts with ID %s...", cart_id)
        cart = super().get_object()
        logger.debug("Fetched carts: %s", cart)
        return cart
