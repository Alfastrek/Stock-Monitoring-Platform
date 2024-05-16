# api/tests.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class WatchlistAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_watchlist_creation(self):
        response = self.client.post('/api/watchlist/', {'symbol': 'AAPL'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Write more test cases for other API endpoints

class StockInfoAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_stock_info_fetching(self):
        response = self.client.get('/api/stock/AAPL/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('symbol', response.data)
        self.assertIn('price', response.data)

    # Write more test cases for other API endpoints
