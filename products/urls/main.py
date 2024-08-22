from products.urls.configurations.main import configuration_routes
from products.urls.products.main import product_routes

urlpatterns = (
    *configuration_routes,
    *product_routes
)

