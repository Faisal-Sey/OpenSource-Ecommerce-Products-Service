from django.urls import path

from products.views.product_views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ProductRetrieveFilterAPIView
)

image_routes = [
    path('',  ProductListCreateAPIView.as_view(), name='products-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('filter/', ProductRetrieveFilterAPIView.as_view(), name='product-filter'),
]