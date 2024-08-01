from django.contrib import admin

from products.models.images_model import Image
from products.models.products_model import (
    Product,
    ProductCurrency,
    ProductLocation,
    ProductDescription,
    ProductSize,
    ProductSizeTitle,
    ProductColorTitle
)
from products.models.menus_model import Menu

admin.site.register(Image)
admin.site.register(Menu)
admin.site.register(ProductCurrency)
admin.site.register(Product)
admin.site.register(ProductColorTitle)
admin.site.register(ProductDescription)
admin.site.register(ProductLocation)
admin.site.register(ProductSize)
admin.site.register(ProductSizeTitle)
