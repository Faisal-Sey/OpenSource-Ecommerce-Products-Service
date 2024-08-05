from django.urls import path

from products.views.cart_views import CartRetrieveUpdateDestroyAPIView, CartListCreateAPIView

carts_routes = [
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart-detail'),
    path('carts/', CartListCreateAPIView.as_view(), name='cart-list-create'),
]
