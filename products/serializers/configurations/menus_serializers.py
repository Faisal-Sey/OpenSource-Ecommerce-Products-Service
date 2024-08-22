from rest_framework import serializers

from products.models.configurations.menus_model import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
