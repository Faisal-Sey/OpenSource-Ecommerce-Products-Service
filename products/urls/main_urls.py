from products.urls.product_urls import image_routes
from products.urls.menu_urls import menu_routes

urlpatterns = [
    *menu_routes,
    *image_routes
]

