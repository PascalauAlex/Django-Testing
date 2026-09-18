from products.models import Product
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# SimpleTest don't touch the database -> better performance
class TestHomePage(SimpleTestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/")

    def test_homepage_uses_correct_template(self):
        self.assertTemplateUsed(response=self.response,template_name="index.html")

    def test_homepage_contains_welcome_message(self):
        self.assertContains(response=self.response,text="Welcome to our Store!",status_code=200)

class TestProductsPage(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000, stock_count=10)
        Product.objects.create(name="Phone", price=800, stock_count=8)
        self.response = self.client.get(reverse('products'))

    def test_products_uses_correct_template(self):
        self.assertTemplateUsed(response=self.response,template_name="products.html")

    def test_products_context(self):
        self.assertEqual(len(self.response.context['products']),2)
        self.assertContains(response=self.response, text="Laptop", status_code=200)
        self.assertContains(response=self.response, text="Phone", status_code=200)
        self.assertNotContains(self.response, text="No products available!")

    def test_products_view_no_products(self):
        Product.objects.all().delete()

        # Create a new request for after the objects are deleted

        response = self.client.get(reverse('products'))
        self.assertContains(response=response, text="No products available!")
        self.assertNotContains(response=response, text="Laptop")
        self.assertNotContains(response=response, text="Phone")
        self.assertEqual(len(response.context['products']), 0)
