from django.test import TestCase, override_settings
from django.urls import reverse


class MaintenanceModeTest(TestCase):
    @override_settings(MAINTENANCE_MODE=False)
    def test_maintenance_mode_off(self):
        """ Test that the site works normally when MAINTENANCE_MODE is False"""
        response = self.client.get(reverse('homepage'))

        #Check that the response is successfull
        self.assertContains(response=response,text='Welcome to our Store!',status_code=200)

    @override_settings(MAINTENANCE_MODE=True)
    def test_maintenance_mode_on(self):
        """ Test that the site works normally when MAINTENANCE_MODE is False"""
        response = self.client.get(reverse('homepage'))

        # Check that the response is successfull
        self.assertContains(response=response, text='Site is under maintenance', status_code=503)

