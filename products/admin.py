from django import forms
from django.contrib import admin
from django_quill.forms import QuillFormField

from products.models.images_model import Image
from products.models.products_model import (
    Product,
    ProductCurrency,
    ProductLocation,
    ProductSize,
    ProductSizeTitle,
    ProductColorTitle
)
from products.models.menus_model import Menu


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
