from django.urls import path

from products.views.products.cart_views import (
    CartRetrieveUpdateDestroyAPIView,
    CartListCreateAPIView,
    AddItemToCartApiView,
    CartItemRetrieveUpdateDestroyAPIView
)

carts_routes = [
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart-detail'),
    path('carts/', CartListCreateAPIView.as_view(), name='cart-list-create'),
    path('carts/add-item/<int:pk>/', AddItemToCartApiView.as_view(), name='add-item-cart'),
    path('carts/cart-item/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view(), name='cart-item-cart'),
]
