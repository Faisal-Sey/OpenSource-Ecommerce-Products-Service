from django.urls import path
from products.views.menu_views import MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('menus/',  MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-detail'),
]