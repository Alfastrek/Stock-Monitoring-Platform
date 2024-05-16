from django.urls import path
from .views import WatchlistAPIView, StockInfoAPIView

urlpatterns = [
    path('watchlist/', WatchlistAPIView.as_view(), name='watchlist'),
    path('stock/<str:symbol>/', StockInfoAPIView.as_view(), name='stock_info'),
]