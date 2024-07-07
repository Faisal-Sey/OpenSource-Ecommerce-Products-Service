from django.test import TestCase

from products.models.menus_model import Menu


class MenuModelTest(TestCase):

    def test_menu_model_fields(self):
        # Create a Menu instance
        menu = Menu.objects.create(title='Test Menu', url='http://example.com')

        # Check if the fields are set correctly
        self.assertEqual(menu.title, 'Test Menu')
        self.assertEqual(menu.url, 'http://example.com')

    def test_menu_model_str_method(self):
        # Create a Menu instance
        menu = Menu.objects.create(title='Test Menu', url='http://example.com')

        # Check the __str__() method returns expected string representation
        self.assertEqual(str(menu), 'Test Menu')

    def test_menu_model_blank_url(self):
        # Create a Menu instance without providing a url
        menu = Menu.objects.create(title='Test Menu')

        # Check if the url field is blank (allowing empty string)
        self.assertEqual(menu.url, '')

    def test_menu_model_max_length_title(self):
        # Test the max length constraint of title field
        max_length = Menu._meta.get_field('title').max_length
        self.assertEqual(max_length, 25)

    # Add more tests as needed for other model validations, constraints, etc.
