from django.test import TestCase
from products.models import Product
from django.urls import reverse

class ProductFormTest(TestCase):

    def test_create_product_when_submitting_valid_form(self):
        """ Test that form submission with valid data creates a product in the database """
        form_data = {
            "name":"Tablet",
            "price":299.99,
            "stock_count":50
        }

        response = self.client.post(path=reverse('products'),data=form_data)
        self.assertEqual(response.status_code,302)
        self.assertTrue(len(Product.objects.all()),1)
        # Check on DB if the product was created
        self.assertTrue(Product.objects.filter(name="Tablet").exists())



    def test_create_product_when_submitting_invalid_form(self):
        """ Test that form submission with invalid data does not create a product. """
        invalid_form_data = {
            "name": " ",
            "price": -1,
            "stock_count": -3
        }

        response = self.client.post(path=reverse('products'), data=invalid_form_data)
        # Check that we get a 200 status ( stay on page to correct errors )
        self.assertEqual(response.status_code,200)
        self.assertTrue("form" in response.context)
        form = response.context['form']
        self.assertFormError(form,field='name',errors='This field is required.')
        self.assertFormError(form, field='price', errors='Price cannot be negative')
        self.assertFormError(form, field='stock_count', errors='Stock count cannot be negative')
        self.assertFalse(Product.objects.all().exists())
