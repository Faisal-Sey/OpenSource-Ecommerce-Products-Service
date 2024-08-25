from typing import Any

from rest_framework import serializers

from config.project_configs import SORT_KEY_CHOICES
from products.models.products.images_model import Image
from products.models.products.products_model import (
    Product,
    ProductColorTitle,
    ProductCurrency,
    ProductLocation,
    ProductSize,
    ProductSizeTitle,
)
from products.serializers.configurations.menus_serializers import MenuSerializer


class ImageSerializer(serializers.ModelSerializer[Image]):  # type: ignore[misc]
    class Meta:
        model = Image
        fields = "__all__"


class ProductLocationsSerializer(
    serializers.ModelSerializer[ProductLocation]  # type: ignore[misc]
):
    class Meta:
        model = ProductLocation
        fields = ("name",)


class ProductCurrencySerializer(
    serializers.ModelSerializer[ProductCurrency]  # type: ignore[misc]
):
    class Meta:
        model = ProductCurrency
        fields = ("name", "symbol")


class ProductSizeTitleSerializer(
    serializers.ModelSerializer[ProductSizeTitle]  # type: ignore[misc]
):
    class Meta:
        model = ProductSizeTitle
        fields = ("id", "title", "disabled")


class ProductColorTitleSerializer(
    serializers.ModelSerializer[ProductColorTitle]  # type: ignore[misc]
):
    class Meta:
        model = ProductColorTitle
        fields = ("id", "title")


class ProductSizeSerializer(
    serializers.ModelSerializer[ProductSize]  # type: ignore[misc]
):
    sizes = ProductSizeTitleSerializer(read_only=True, many=True)
    color = ProductColorTitleSerializer(read_only=True)

    class Meta:
        model = ProductSize
        fields = ("id", "color", "sizes", "disabled")


class ListProductSerializer(serializers.ModelSerializer[Product]):  # type: ignore[misc]
    featured_image = ImageSerializer(read_only=True)
    currency = ProductCurrencySerializer(read_only=True)

    class Meta:
        model = Product
        exclude = (
            "images",
            "product_type",
            "product_locations",
            "description",
            "created_on",
            "updated_on",
        )


class SingleProductSerializer(
    serializers.ModelSerializer[Product]  # type: ignore[misc]
):
    images = ImageSerializer(many=True, read_only=True)
    product_locations = ProductLocationsSerializer(many=True, read_only=True)
    product_type = MenuSerializer(many=True, read_only=True)
    featured_image = ImageSerializer(read_only=True)
    currency = ProductCurrencySerializer(read_only=True)
    description = serializers.CharField(source="description.html")

    def to_representation(self, instance: Product) -> Any:
        data = super().to_representation(instance)
        data["sizes"] = ProductSizeSerializer(
            instance.product_size.all(), many=True
        ).data
        return data

    class Meta:
        model = Product
        fields = "__all__"


class ProductSearchListSerializer(serializers.Serializer):  # type: ignore[misc]
    query = serializers.CharField(required=False, default="")
    reverse = serializers.BooleanField(required=False, default=False)
    sort_key = serializers.ChoiceField(
        required=False, choices=SORT_KEY_CHOICES, default="price"
    )
    page_number = serializers.IntegerField(required=False, default=1)
    items_per_page = serializers.IntegerField(required=False, default=10)
    custom_query = serializers.DictField(required=False, default={})
