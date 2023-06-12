from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.

class SimpleTest(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_products_status_code(self):
        response = self.client.get('/products/')
        self.assertEquals(response.status_code, 200)

    def test_ads_status_code(self):
        response = self.client.get('/ads/')
        self.assertEquals(response.status_code, 200)

