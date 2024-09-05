from typing import Any

from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from products.models.configurations.menus_model import Menu
from products.serializers.configurations.menus_serializers import MenuSerializer
from utils.logger.logger_handler import logger


class MenuListCreateAPIView(ListCreateAPIView):  # type: ignore[misc]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self) -> Any:
        logger.debug("Fetching menu list...")
        queryset = super().get_queryset().filter(hidden=False)
        logger.debug("Fetched %d menu items", queryset.count())
        return queryset


class MenuGetUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):  # type: ignore[misc]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_object(self) -> Menu:
        menu_id = self.kwargs.get("pk")
        logger.debug("Fetching menu with ID %s...", menu_id)
        menu: Menu = super().get_object()
        logger.debug("Fetched menu: %s", menu)
        return menu


class MenuByTitleSingleAPIView(RetrieveUpdateDestroyAPIView):  # type: ignore[misc]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_object(self) -> Menu:
        menu_title = self.kwargs.get("menu_title")
        logger.debug("Fetching menu with title %s...", menu_title)

        # Filter the queryset by name
        try:
            menu = self.queryset.get(title__iexact=menu_title)
            logger.debug("Fetched menu: %s", menu)
            return menu
        except Menu.DoesNotExist:
            logger.error("Menu with name %s not found", menu_title)
            raise Http404("Menu not found")
