from os import name
from unittest.mock import patch

from django.contrib.auth.models import AbstractUser
from django.db.models import Model

from products.models import User
from django.test import TestCase



class UserSignalsTest(TestCase):
    @patch('products.signals.send_mail')
    def test_user_email_send_on_user_creation(self, mock_send_mail):
        # Create a new user witch should trigger the signal
        User.objects.create(username="test",password="test",email="test@test.com")

        #Check the send_mail was called once
        mock_send_mail.assert_called_once_with(
            subject='Welcome!',
            message="Thanks for signing ",
            from_email="admin@django.com",
            recipient_list=['test@test.com'],
            fail_silently=False
        )

    @patch('products.signals.send_mail')
    def test_user_email_send_on_user_update(self, mock_send_mail):
        # Create a new user witch should trigger the signal
        user = User.objects.create(username="test", password="test", email="test@test.com")

        # Reset the mock call count to zero
        mock_send_mail.reset_mock()

        # Update the user (the signal should not send an email this time)

        user.email = "john@test.com"
        user.save()

        mock_send_mail.assert_not_called()



