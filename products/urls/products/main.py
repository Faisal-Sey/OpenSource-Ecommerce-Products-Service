from products.urls.products.cart_urls import carts_routes
from products.urls.products.product_urls import image_routes

product_routes = (
    *image_routes,
    *carts_routes,
)