from django.urls import path

from products.views.configurations.menu_views import (
    MenuByTitleSingleAPIView,
    MenuGetUpdateDestroyAPIView,
    MenuListCreateAPIView,
)

menu_routes = (
    path("menus/", MenuListCreateAPIView.as_view(), name="menu-list-create"),
    path(
        "menus/title/<str:menu_title>/",
        MenuByTitleSingleAPIView.as_view(),
        name="menu-title-detail",
    ),
    path(
        "menus/<int:pk>/",
        MenuGetUpdateDestroyAPIView.as_view(),
        name="menu-detail",
    ),
)
