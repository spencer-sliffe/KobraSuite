from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    """
    A user’s investment portfolio.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='portfolios'
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Asset(models.Model):
    """
    Represents an investable asset (stock, ETF, crypto, etc.).
    """

    symbol = models.CharField(max_length=50, unique=True)
    asset_type = models.CharField(max_length=50, choices=AssetType.choices, default=AssetType.OTHER)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.symbol} - {self.asset_type}"


class Holding(models.Model):
    """
    Through table between Portfolio and Asset to track quantity/cost basis.
    """
    portfolio = models.ForeignKey(
        Portfolio, 
        on_delete=models.CASCADE, 
        related_name='holdings'
    )
    asset = models.ForeignKey(
        Asset, 
        on_delete=models.CASCADE, 
        related_name='holdings'
    )
    quantity = models.DecimalField(max_digits=12, decimal_places=4, default=0.0000)
    average_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0.0000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.portfolio.name} - {self.asset.symbol}"


class TradeTransaction(models.Model):
    """
    Records buy/sell transactions for a holding.
    """
    holding = models.ForeignKey(
        Holding, 
        on_delete=models.CASCADE, 
        related_name='transactions'
    )
    transaction_type = models.CharField(max_length=4, choices=TradeTransactionType.choices)
    quantity = models.DecimalField(max_digits=12, decimal_places=4)
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=4)
    transaction_date = models.DateTimeField()
    fees = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.holding.asset.symbol}"


class Watchlist(models.Model):
    """
    A user’s watchlist of assets to track.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='watchlists'
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    assets = models.ManyToManyField(Asset, related_name='watchlisted_by', blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class MarketData(models.Model):
    """
    Stores daily or real-time data for an asset.
    """
    asset = models.ForeignKey(
        Asset, 
        on_delete=models.CASCADE, 
        related_name='market_data'
    )
    date = models.DateField()
    open_price = models.DecimalField(max_digits=12, decimal_places=4)
    high_price = models.DecimalField(max_digits=12, decimal_places=4)
    low_price = models.DecimalField(max_digits=12, decimal_places=4)
    close_price = models.DecimalField(max_digits=12, decimal_places=4)
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.asset.symbol} - {self.date}"

