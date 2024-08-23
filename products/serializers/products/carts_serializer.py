from typing import Any

from rest_framework import serializers

from products.models.products.products_model import (
    Product,
    ProductCart,
    ProductCartItem,
    ProductCurrency,
)
from products.serializers.products.product_serializer import (
    ImageSerializer,
    ProductCurrencySerializer,
)


class CartProductSerializer(serializers.ModelSerializer[Product]):  # type: ignore[misc]
    featured_image = ImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "name", "price", "featured_image")


class ProductCartItemSerializer(
    serializers.ModelSerializer[ProductCartItem]  # type: ignore[misc]
):
    product = CartProductSerializer(required=True)
    image = ImageSerializer(required=True)

    class Meta:
        model = ProductCartItem
        fields = "__all__"


class ProductCartSerializer(
    serializers.ModelSerializer[ProductCart]  # type: ignore[misc]
):
    cart_items = ProductCartItemSerializer(many=True, required=False)
    currency = serializers.PrimaryKeyRelatedField(
        queryset=ProductCurrency.objects.all()
    )
    currency_details = ProductCurrencySerializer(
        read_only=True, source="currency", required=False
    )

    class Meta:
        model = ProductCart
        fields = "__all__"

    def to_representation(self, instance: ProductCart) -> Any:
        data = super().to_representation(instance)
        data["currency"] = self.fields["currency_details"].to_representation(
            instance.currency
        )
        data.pop("currency_details")
        return data


class AddItemToCartSerializer(serializers.Serializer):  # type: ignore[misc]
    product_id = serializers.IntegerField()
    image_id = serializers.IntegerField()
    total_amount = serializers.FloatField()
    quantity = serializers.IntegerField()
    product_size = serializers.JSONField()
