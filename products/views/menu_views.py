from typing import Any
from rest_framework import generics

from utils.logger.logger_handler import logger
from products.models.menus_model import Menu
from products.serializers.menus_serializers import MenuSerializer


class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self) -> Any:
        logger.debug("Fetching menu list...")
        queryset = super().get_queryset()
        logger.debug("Fetched %d menu items", queryset.count())
        return queryset


class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_object(self) -> Menu:
        menu_id = self.kwargs.get('pk')
        logger.debug("Fetching menu with ID %s...", menu_id)
        menu = super().get_object()
        logger.debug("Fetched menu: %s", menu)
        return menu
