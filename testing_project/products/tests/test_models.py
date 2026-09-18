from django.test import TestCase
from django.core.exceptions import ValidationError
from products.models import Product
from django.db import IntegrityError

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.product = Product(name="Test Product", price=100.00, stock_count = 10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)
        # reset product stock to 0
        self.product.stock_count = 0
        self.assertFalse(self.product.in_stock)

    def test_discount_price(self):
        self.assertEqual(self.product.get_discounted_price(discount_percentage=10), 90)
        self.assertEqual(self.product.get_discounted_price(discount_percentage=50), 50)
        self.assertEqual(self.product.get_discounted_price(discount_percentage=100), 0)
        self.assertEqual(self.product.get_discounted_price(discount_percentage=0),100)

    def test_negative_price_validation(self):
        self.product.price = -10
        # Context manager
        with self.assertRaises(expected_exception=ValidationError):
            self.product.clean()

    def test_negative_stock_validation(self):
        self.product.stock_count = -10
        # Context manager
        with self.assertRaises(expected_exception=ValidationError):
            self.product.clean()

    def test_negative_price_constraint(self):
        """ Test a product with negative price cannot be saved due to database constraint """
        product = Product(name="Negative price product", price=-5, stock_count=10)
        with self.assertRaises(expected_exception=IntegrityError):
            product.save()

    def test_negative_stock_count_constraint(self):
        """ Test a product with negative stock_count cannot be saved due to database constraint """
        product = Product(name="Negative stock_count product", price=100.00, stock_count=-5)
        with self.assertRaises(expected_exception=IntegrityError):
            product.save()


