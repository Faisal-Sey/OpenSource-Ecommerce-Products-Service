from django.contrib import admin

from products.models.products.images_model import Image
from products.models.products.products_model import (
    Product,
    ProductCurrency,
    ProductLocation,
    ProductSize,
    ProductSizeTitle,
    ProductColorTitle, ProductCart, ProductCartItem
)
from products.models.configurations.menus_model import Menu


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image)
admin.site.register(Menu)
admin.site.register(ProductCurrency)
admin.site.register(ProductColorTitle)
admin.site.register(ProductLocation)
admin.site.register(ProductSize)
admin.site.register(ProductSizeTitle)
admin.site.register(ProductCart)
admin.site.register(ProductCartItem)
