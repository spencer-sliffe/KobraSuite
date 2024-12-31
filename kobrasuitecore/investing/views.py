from rest_framework import viewsets
from .models import Portfolio, Asset, TradeTransaction

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    # serializer_class = PortfolioSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    # serializer_class = AssetSerializer

class TradeTransactionViewSet(viewsets.ModelViewSet):
    queryset = TradeTransaction.objects.all()
    # serializer_class = TradeTransactionSerializer