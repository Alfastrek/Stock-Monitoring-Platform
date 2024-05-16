# api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Watchlist
from .serializers import WatchlistSerializer
from .utils import fetch_stock_price
from rest_framework import generics
import requests

class WatchlistAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        watchlists = Watchlist.objects.filter(user=request.user)
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk, user=request.user)
            watchlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)

class StockInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        watchlists = Watchlist.objects.filter(user=request.user)
        symbols = [watchlist.symbol for watchlist in watchlists]
        stock_prices = {}
        for symbol in symbols:
            stock_price = fetch_stock_price(symbol)
            if stock_price is not None:
                stock_prices[symbol] = stock_price
        return Response(stock_prices, status=status.HTTP_200_OK)
    