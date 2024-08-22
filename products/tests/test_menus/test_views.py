from typing import Any
from django.test import TestCase, RequestFactory
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from products.models.configurations.menus_model import Menu
from products.views import handler404, MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView


class Test404Handler(TestCase):
    def setUp(self) -> None:
        self.factory: RequestFactory = RequestFactory()

    def test_404_handler(self) -> None:
        request: HttpRequest = self.factory.get('/some-invalid-url/')
        response: HttpResponse = handler404(request, Exception())
        self.assertEqual(response.status_code, 404)


class TestMenuListCreateAPIView(TestCase):
    def setUp(self) -> None:
        self.factory: APIRequestFactory = APIRequestFactory()
        self.view: Any = MenuListCreateAPIView.as_view()
        self.url: str = reverse('menu-list-create')  # Ensure this matches your URL configuration

    def test_get_menu_list(self) -> None:
        request: HttpRequest = self.factory.get(self.url)
        response: HttpResponse = self.view(request)
        self.assertEqual(response.status_code, 200)  # Assuming successful response code

    # Add more tests as needed for create functionality


class TestMenuRetrieveUpdateDestroyAPIView(TestCase):
    def setUp(self) -> None:
        self.factory: APIRequestFactory = APIRequestFactory()
        self.menu: Menu = Menu.objects.create(title='Test Menu', url='http://example.com')
        self.view: Any = MenuRetrieveUpdateDestroyAPIView.as_view()
        self.url: str = reverse('menu-detail', kwargs={'pk': self.menu.pk})  # Ensure this matches your URL configuration

    def test_get_menu_detail(self) -> None:
        request: HttpRequest = self.factory.get(self.url)
        response: HttpResponse = self.view(request, pk=self.menu.pk)
        self.assertEqual(response.status_code, 200)  # Assuming successful response code

    # Add more tests as needed for update and delete functionality
