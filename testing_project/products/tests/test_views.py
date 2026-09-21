from products.models import Product, User
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
import requests


class PostViewTest(TestCase):
    @patch('products.views.requests.get') # We either get a AsyncMock either a MagicMock obj
    def test_view_success(self, mock_get : MagicMock):
        """ Simulate the actual data , status code , etc.,
            that is provided by the external service"""

        mock_get.return_value.status_code = 200
        return_data = {
            "userId":1,
            "id":1,
            "title":"Test Title",
            "body":"Test Body"
        }
        mock_get.return_value.json.return_value = return_data
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code,200)
        self.assertJSONEqual(response.content,return_data)

        # Ensure that the mock API call was made once with the correct URL
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')


    @patch('products.views.requests.get')
    def test_post_view_fail(self,mock_get: MagicMock):
        """ Test that the posts view returns a 503 on HTTP errors. """
        mock_get.side_effect = requests.exceptions.RequestException

        # Send a request to the view
        response = self.client.get(reverse('post'))
        # Check that the view returns a 503 Service Unavailable status code
        self.assertEqual(response.status_code,503)
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')


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

class TestProfilePage(TestCase):

    def test_profile_view_not_accessible_for_unauthenticated_users(self):
        response = self.client.get(reverse('profile'))
        # If not authenticated the user will be redirected to '/login/?next=/profile', so we can't access contains
        # The response contains data loaded only for the profile page, but since we got redirected, the page is empty
        print(f'Response content: ',response.content) # Empty page
        self.assertRedirects(response,expected_url=f"{reverse('login')}?next={reverse('profile')}")


    def test_profile_view_accessible_for_authenticated_users(self):
        # Create a test user
        user = User.objects.create(username="test_user", password="password123")

        # Log the user in
        self.client.force_login(user=user)
        response = self.client.get(reverse('profile'))

        #Check if the user username is into the response content
        self.assertContains(response=response, text="test_user")

