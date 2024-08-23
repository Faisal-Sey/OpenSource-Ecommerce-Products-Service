from django.db import models
from django_quill.fields import QuillField

from common.base_model import BaseModel


class ProductLocation(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Product Locations"


class ProductCurrency(BaseModel):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.symbol

    class Meta:
        verbose_name_plural = "Product Currencies"


class ProductColorTitle(BaseModel):
    title = models.CharField(max_length=500)
    hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Product Color Titles"


class ProductSizeTitle(BaseModel):
    title = models.CharField(max_length=500)
    disabled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Product Size Titles"


class ProductSize(BaseModel):
    product = models.ForeignKey(
        "products.Product",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="product_size",
    )
    sizes = models.ManyToManyField(
        "products.ProductSizeTitle", blank=True, related_name="product_size_tile"
    )
    color = models.ForeignKey(
        "products.ProductColorTitle",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="product_color_tile",
    )
    disabled = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.product is not None:
            return (
                f"{self.product} - {self.color.title}"
                if (self.product and self.color)
                else self.product.name
            )
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Product Sizes"


class ProductCartItem(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="cart_item_product"
    )
    image = models.ForeignKey(
        "products.Image",
        on_delete=models.CASCADE,
        related_name="cart_item_product_image",
    )
    quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0.0)
    product_size = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.product.name


class ProductCart(BaseModel):
    checkout_url = models.URLField(blank=True)
    cart_items = models.ManyToManyField(
        "products.ProductCartItem", blank=True, related_name="product_cart_item"
    )
    total_amount = models.FloatField(default=0.0)
    total_taxed = models.FloatField(default=0.0)
    total_quantity = models.IntegerField(default=0)
    currency = models.ForeignKey(
        "products.ProductCurrency",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="product_cart_currency",
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.total_amount}"


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    description = QuillField(blank=True, null=True)
    images = models.ManyToManyField(
        "products.Image", blank=True, related_name="product_images"
    )
    featured_image = models.ForeignKey(
        "products.Image",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="product_feature_image",
    )
    price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    min_price = models.FloatField(default=0.0)
    currency = models.ForeignKey(
        "products.ProductCurrency",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="product_currency",
    )
    url = models.URLField(blank=True)
    for_sale = models.BooleanField(default=True)
    product_type = models.ManyToManyField("products.Menu", related_name="product_menus")
    product_locations = models.ManyToManyField(
        "products.ProductLocation", blank=True, related_name="product_locations"
    )

    def __str__(self) -> str:
        return self.name
