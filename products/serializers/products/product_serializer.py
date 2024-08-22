from rest_framework import serializers

from products.models.products.images_model import Image
from products.models.products.products_model import (
    Product,
    ProductLocation,
    ProductCurrency,
    ProductSize,
    ProductColorTitle,
    ProductSizeTitle, ProductCart, ProductCartItem
)
from products.serializers.configurations.menus_serializers import MenuSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLocation
        fields = ('name',)


class ProductCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCurrency
        fields = ('name', 'symbol')


class ProductSizeTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizeTitle
        fields = ('id', 'title', 'disabled')


class ProductColorTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColorTitle
        fields = ('id', 'title')


class ProductSizeSerializer(serializers.ModelSerializer):
    sizes = ProductSizeTitleSerializer(read_only=True, many=True)
    color = ProductColorTitleSerializer(read_only=True)

    class Meta:
        model = ProductSize
        fields = ('id', 'color', 'sizes', 'disabled')


class ListProductSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer(read_only=True)
    currency = ProductCurrencySerializer(read_only=True)

    class Meta:
        model = Product
        exclude = (
            'images',
            'product_type',
            'product_locations',
            'description',
            'created_on',
            'updated_on'
        )


class SingleProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    product_locations = ProductLocationsSerializer(many=True, read_only=True)
    product_type = MenuSerializer(many=True, read_only=True)
    featured_image = ImageSerializer(read_only=True)
    currency = ProductCurrencySerializer(read_only=True)
    description = serializers.CharField(source='description.html')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['sizes'] = ProductSizeSerializer(instance.product_size.all(), many=True).data
        return data

    class Meta:
        model = Product
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'featured_image')


class ProductCartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(required=True)
    image = ImageSerializer(required=True)

    class Meta:
        model = ProductCartItem
        fields = '__all__'


class ProductCartSerializer(serializers.ModelSerializer):
    cart_items = ProductCartItemSerializer(many=True, required=False)
    currency = serializers.PrimaryKeyRelatedField(queryset=ProductCurrency.objects.all())
    currency_details = ProductCurrencySerializer(read_only=True, source='currency', required=False)

    class Meta:
        model = ProductCart
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['currency'] = self.fields['currency_details'].to_representation(instance.currency)
        data.pop('currency_details')
        return data


class AddItemToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    image_id = serializers.IntegerField()
    total_amount = serializers.FloatField()
    quantity = serializers.IntegerField()
    product_size = serializers.JSONField()
