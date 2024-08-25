from django.urls import path

from products.views.products.product_views import (
    ProductListAPIView,
    ProductListCreateAPIView,
    ProductRetrieveFilterAPIView,
    ProductRetrieveUpdateDestroyAPIView,
)

image_routes = [
    path("", ProductListCreateAPIView.as_view(), name="products-list-create"),
    path(
        "<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-detail",
    ),
    path("filter/", ProductRetrieveFilterAPIView.as_view(), name="product-filter"),
    path("search/", ProductListAPIView.as_view(), name="product-search"),
]
