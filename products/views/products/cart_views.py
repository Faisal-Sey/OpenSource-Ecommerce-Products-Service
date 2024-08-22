from typing import Any, Dict

from django.db import transaction
from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from products.models.products.products_model import ProductCart, ProductCartItem
from products.serializers.products.product_serializer import (
    ProductCartSerializer, AddItemToCartSerializer, ProductCartItemSerializer
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
        cart = super().get_object()
        logger.info("Fetched cart: %s", cart)
        return cart


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCartItem.objects.all()
    serializer_class = ProductCartItemSerializer

    def get_object(self) -> ProductCartItem:
        cart_item = super().get_object()
        logger.info("Fetched cart: %s", cart_item)
        return cart_item

    @transaction.atomic
    def perform_destroy(self, instance: ProductCartItem):
        # Log the deletion action
        logger.info("Deleting cart item: %s", instance)

        # Perform additional actions after deletion
        self.pre_delete_action(instance)

        # Perform the deletion
        super().perform_destroy(instance)

        logger.info("Deleted cart item: %s", instance)

    @staticmethod
    def pre_delete_action(instance: ProductCartItem):
        # Example: Decrease the total quantity in the ProductCart after deletion
        carts = ProductCart.objects.filter(cart_items__in=[instance])
        logger.info("Carts to reduce total amount: %s", carts)
        carts.update(total_amount=F('total_amount') - instance.total_amount)

        # Additional actions can be added here
        logger.info("Post-delete cart item completed for cart item: %s", instance)


class AddItemToCartApiView(generics.GenericAPIView):
    queryset = ProductCart.objects.all()
    serializer_class = AddItemToCartSerializer

    def get_object(self) -> ProductCart:
        cart = super().get_object()
        logger.info("Fetched cart: %s", cart)
        return cart

    def patch(self, request, *args, **kwargs):
        data: Dict[str, Any] = request.data
        logger.info("validated_data: %s", data)
        new_cart_items = data.get("cart_items", [])

        cart = self.get_object()
        logger.info("Cart: %s", cart)

        for new_cart_item in new_cart_items:
            cart_items = cart.cart_items.filter(
                product_id=new_cart_item.get('product_id'),
                image_id=new_cart_item.get('image_id')
            )

            new_item_product_size = new_cart_item.get('product_size', {})

            logger.info("new item product size: %s", new_item_product_size)

            matching_cart_items = [
                item for item in cart_items
                if all(item.product_size.get(k) == v for k, v in new_item_product_size.items())
            ]

            logger.info("matching cart items: %s", matching_cart_items)

            if not len(matching_cart_items):
                cart_item = ProductCartItem.objects.create(**new_cart_item)
                cart.cart_items.add(cart_item)
                logger.info("new cart item: %s", cart_item.id)
            else:
                # update the cart item
                cart_item: ProductCartItem = cart_items.first()
                cart_item.quantity += new_cart_item.get('quantity', 0)
                cart_item.total_amount += new_cart_item.get('total_amount', 0)
                cart_item.image_id = new_cart_item.get('image_id', cart_item.image_id)
                cart_item.save()

            logger.info("Cart item updated: %s", cart_item.id)

            # update the cart
            cart.total_amount += new_cart_item.get('total_amount', 0.0)

            logger.info("cart updated: %s", cart.id)

        cart.save()
        return Response({"message": "Cart updated successfully"}, status=HTTP_200_OK)
