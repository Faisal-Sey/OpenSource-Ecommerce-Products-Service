from django.db import models

from common.base_model import BaseModel


class ProductLocation(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Locations"


class ProductCurrency(BaseModel):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name_plural = "Product Currencies"


class ProductDescription(BaseModel):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Product Description"


class ProductColorTitle(BaseModel):
    title = models.CharField(max_length=500)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product Color Titles"


class ProductSizeTitle(BaseModel):
    title = models.CharField(max_length=500)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product Size Titles"


class ProductSize(BaseModel):
    product = models.ForeignKey(
        "products.Product",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="product_size"
    )
    sizes = models.ManyToManyField(
        "products.ProductSizeTitle",
        blank=True,
        related_name="product_size_tile"
    )
    color = models.ForeignKey(
        "products.ProductColorTitle",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="product_color_tile"
    )
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.color.title}" \
            if (self.product and self.color) else self.product.name

    class Meta:
        verbose_name_plural = "Product Sizes"


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    description = models.ManyToManyField(
        "products.ProductDescription",
        related_name="product_description"
    )
    images = models.ManyToManyField(
        "products.Image",
        blank=True,
        related_name="product_images"
    )
    featured_image = models.ForeignKey(
        "products.Image",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="product_feature_image"
    )
    price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    min_price = models.FloatField(default=0.0)
    currency = models.ForeignKey(
        "products.ProductCurrency",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="product_currency"
    )
    url = models.URLField(blank=True)
    for_sale = models.BooleanField(default=True)
    product_type = models.ManyToManyField(
        "products.Menu",
        related_name="product_menus"
    )
    product_locations = models.ManyToManyField(
        "products.ProductLocation",
        blank=True,
        related_name="product_locations"
    )

    def __str__(self):
        return self.name
