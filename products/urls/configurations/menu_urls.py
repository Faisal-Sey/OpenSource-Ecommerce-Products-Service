from django.urls import path
from products.views.configurations.menu_views import MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView

menu_routes = (
    path('menus/',  MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-detail'),
)